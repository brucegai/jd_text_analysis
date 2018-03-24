# -*- coding: utf-8 -*-
import requests as rq
import re, os, time, urllib, json,random,csv
from bs4 import BeautifulSoup
from urllib import parse
from sqlalchemy import create_engine
from sqlalchemy.orm import session
"""this script is to get all comments of lenovo pc product"""

jd_url = "https://lenovo1.jd.com/"
apple_url="https://apple.jd.com/"
agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
def get_lenovo_list():
    type_list = []
    comment_url_list = []
    filter_url_list=[]
    response = rq.get(jd_url)
    soup = BeautifulSoup(response.text, "html.parser")
    item_list = soup.select('map area')
    for item in item_list:
        website = item.attrs['href']
        if re.search('list', website) != None or re.search('mall', website) != None:
            type_list.append(website)
    for i in range(len(type_list)):
        result = BeautifulSoup(rq.get("http:" + type_list[i]).content, "html.parser")
        url_tag = result.select(".gl-item")
        for url_list in url_tag:
            for url_list_2 in url_list.find_all('a'):
                item_website = url_list_2.attrs['href']
                if re.search('item.jd.com', item_website) != None:
                    comment_url_list.append(item_website)
    for i in range(len(comment_url_list)):
        if comment_url_list[i]!=comment_url_list[i-1]:
            filter_url_list.append(comment_url_list[i])
    # print(filter_url_list)
    return filter_url_list

def get_comments():
    """get comments
    翻页爬取logic：1.遍历item_url 获取item_id 2.每一个item_id 下遍历page number爬取评论文本"""
    item_url = get_lenovo_list()
    comment_list=[]
    for i in range(len(item_url)):
        time.sleep(random.randint(10,20))
        item_id=re.findall(r'\d+',item_url[i])
        print(item_id)
        # comment_list.append(item_id)
        """get page number undone,use 50 page as default"""
        for k in range(0,2):
            another_page_url="http://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv8661&productId="+str(item_id[0])+"&score=0&sortType=5&page="+str(k)+"&pageSize=10&isShadowSku=0&rid=0&fold=1"
            l=rq.session()
            page_content=(l.get(another_page_url).text).replace('fetchJSON_comment98vv8661(','')
            json_docs=json.loads(page_content.replace(');',''))
            for json_doc in json_docs['comments']:
                time.sleep(random.randint(15,30))
                comment_list.append([json_doc['referenceTime'],json_doc['referenceName'],json_doc['userLevelName'],json_doc['usefulVoteCount'],json_doc['content']])
                print(json_doc['referenceName'])
            time.sleep(random.randint(5,10))
            print(k)

    with open('C:/jd_text/test_1.csv', 'w', newline="",encoding='utf-8') as csvwriter:
        csv_writer_2 = csv.writer(csvwriter)
        for comment in comment_list:
            csv_writer_2.writerow(comment)
    return comment_list

def store_in_mysql(list_a):
    """connect to mysql server function"""
    transfer_list=list_a

# get_comments()
get_lenovo_list()

"""1.翻页爬取 (done)
    2.获得每个item 有评论的页数(未完成，通过 3.动态网页爬取 4.模拟登陆 """
"""fake jd login, ask github project: huangfs@bupt.edu.cn"""