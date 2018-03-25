# -*- coding: utf-8 -*-
import csv
path="C:/jd_text/"
""""remove all ‘/’"""
def import_data():
    list_a=[]
    with open (path+'lenovo_1_cut_result.csv','r',encoding='gbk')as csvreader:
        csv_reader=csv.reader(csvreader)
        for line in csv_reader:
            each_word=line[0].split('/')
            for i in range(len(each_word)):
                list_a.append(each_word[i])
    with open('C:/jd_text/word_for_analysis_3.csv', 'w', newline="",encoding='utf-8') as csvwriter:
        csv_writer_2 = csv.writer(csvwriter)
        for line in list_a:
            csv_writer_2.writerow([line])
import_data()
