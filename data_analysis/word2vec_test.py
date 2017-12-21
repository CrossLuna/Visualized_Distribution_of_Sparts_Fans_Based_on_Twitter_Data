from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
#from pyspark.ml.evaluation import RegressionEvaluator
#from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
#from pyspark.ml.feature import StringIndexer

from pyspark.streaming import StreamingContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.clustering import StreamingKMeans

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.datasets import dump_svmlight_file
from sklearn.datasets import *
import numpy as np
import os
import json

from pyspark.mllib.feature import Word2Vec, Word2VecModel

#import text_proc 
from text_proc import clean_text


#conf = SparkConf().setAppName("Jack").setMaster("local")
conf = SparkConf().setAppName("Jack").setMaster("local").set('spark.driver.memory', '6G').set('spark.driver.maxResultSize', '10G')
sc = SparkContext.getOrCreate(conf = conf)
spark = SparkSession.builder.appName("Python Spark SQL Example").getOrCreate()

#word2vec = Word2Vec()
#word2vec_model = Word2VecModel()
#word2vec.load(sc, "text8_long.mdl")
model = Word2VecModel.load(sc, "text8_long.mdl")
#synonyms = model.findSynonyms('team', 10)

#for word, cosine_distance in synonyms:
#    print ("{}: {}".format(word, cosine_distance))
#vec = model.transform('good')
#print(len(vec))
#vec = model.transform('bad')
#print(len(vec))
#vec = model.transform('smart')
#print(len(vec))

if __name__ == "__main__":
    filename = 'all_tweets_text.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    cnt = 1
    twvecs = []
    for line in lines:
        #print ("COUNT " + str(cnt))
        #print (line)
        twvec = [0.0] * 100
        c_line = clean_text(line)
        word_cnt = 0
        for w in c_line:
            try:
                vec = model.transform(w)
                for i in range(len(twvec)):
                    twvec[i] += vec[i] * 1000.0
                    word_cnt += 1
            except:
                pass

        if word_cnt > 0:
            for i in range(len(twvec)):
                twvec[i] /= word_cnt;
            twvecs.append(twvec)
        cnt += 1
    
#print(twvecs)
#print(cnt)
#print(len(twvecs))

def tweet_vectors_from_json(fname = 'all_tweets_list.json'):
    #filename = 'all_tweets_text.txt'
    #filename = 'all_tweets_text.txt'
    filename = fname
    file = open(filename, 'r')
    lines = file.readlines()
    data = json.load(open(filename))
    cnt = 1
    twvecs = []
    for d in data:
        twvec = [0.0] * 100
        line = d['text']
        c_line = clean_text(line)
        word_cnt = 0
        for w in c_line:
            try:
                vec = model.transform(w)
                for i in range(len(twvec)):
                    twvec[i] += vec[i] * 1000.0
                    word_cnt += 1
            except:
                pass

        if word_cnt > 0:
            for i in range(len(twvec)):
                twvec[i] /= word_cnt;
            twvecs.append(twvec)
        cnt += 1
    '''
    for line in lines:
        twvec = [0.0] * 100
        c_line = clean_text(line)
        word_cnt = 0
        for w in c_line:
            try:
                vec = model.transform(w)
                for i in range(len(twvec)):
                    twvec[i] += vec[i] * 1000.0
                    word_cnt += 1
            except:
                pass

        if word_cnt > 0:
            for i in range(len(twvec)):
                twvec[i] /= word_cnt;
            twvecs.append(twvec)
        cnt += 1
    '''
    return twvecs


def tweet_vectors(fname = 'all_tweets_text.txt'):
    #filename = 'all_tweets_text.txt'
    #filename = 'all_tweets_text.txt'
    filename = fname
    file = open(filename, 'r')
    lines = file.readlines()
    cnt = 1
    twvecs = []
    for line in lines:
        twvec = [0.0] * 100
        c_line = clean_text(line)
        word_cnt = 0
        for w in c_line:
            try:
                vec = model.transform(w)
                for i in range(len(twvec)):
                    twvec[i] += vec[i] * 1000.0
                    word_cnt += 1
            except:
                pass

        if word_cnt > 0:
            for i in range(len(twvec)):
                twvec[i] /= word_cnt;
            twvecs.append(twvec)
        cnt += 1
    return twvecs