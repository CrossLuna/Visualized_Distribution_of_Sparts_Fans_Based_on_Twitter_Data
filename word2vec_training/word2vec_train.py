from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import Row

from pyspark.streaming import StreamingContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.clustering import StreamingKMeans

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.datasets import dump_svmlight_file
from sklearn.datasets import *
import numpy as np
import os

from pyspark.mllib.feature import Word2Vec

##initial setting

conf = SparkConf().setAppName("Jack").setMaster("local").set('spark.driver.memory', '6G').set('spark.driver.maxResultSize', '10G')
sc = SparkContext.getOrCreate(conf = conf)
spark = SparkSession.builder.appName("Python Spark SQL Example").getOrCreate()


## training file for word2vec
## http://mattmahoney.net/dc/text8.zip
file_path = 'text8'
inp = sc.textFile(file_path).map(lambda row: row.split(" "))
word2vec = Word2Vec()
model = word2vec.fit(inp)

## save the model to avoid duplicate training
model.save(sc, "text8_long.mdl")