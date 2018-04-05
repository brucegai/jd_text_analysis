import tensorflow as tf
import numpy,csv,scipy,re
import matplotlib as mtb
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
path="E:/jd_text/"

class tf_test:
    """self default parameters of model"""
    def __init__(self,x,y):
        self.learning_rate=0.001
        self.batch_size=5
        self.sentence_length=100
        self.min_size_word=2
        self.echo_times=3
        self.num_layer=3
        self.num_class=10
        self.x=x
        self.y=y
        self.word_dim=3

    def softmax_fuc(self,x):
        return numpy.exp(x-numpy.max(x))/numpy.sum(numpy.exp(x-numpy.max(x)))

    def process_data(self):
        word_2_vec=[]
        with open ('C:/jd_text/dict/comma_dictionary.csv','r',encoding='gbk')as csvreader:
            csv_reader=csv.reader(csvreader)
            for line in csv_reader:
                print(line)
                # for i in range(len(line)):
                #     line_seg=line[i].split('/s')
                #     for k in range(len(line_seg)):
                #         if len(line[i].split('/s')[k])>2:
                word_2_vec.append(line)
        model_init=word2vec.Word2Vec(sentences=word_2_vec,size=self.sentence_length,window=5,min_count=self.min_size_word,workers=4,alpha=self.learning_rate)
        model_init.save('C:/jd_text/model/model_one.model')
        model=word2vec.Word2Vec.load('C:/jd_text/model/model_one.model')
        return model

    def initial_vector(self):
        vector=tf_test(10,9)
        vector_init=vector.process_data()
        print(vector_init.wv["京东"])


if __name__ == '__main__':
        test1=tf_test(10,9)
        test1.initial_vector()


