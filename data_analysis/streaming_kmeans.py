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
import sys

from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
#from pyspark.ml.evaluation import RegressionEvaluator
#from pyspark.ml.recommendation import ALS
from pyspark.streaming import StreamingContext
from pyspark.sql import Row

from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.clustering import StreamingKMeans

from word2vec_test import tweet_vectors
from word2vec_test import tweet_vectors_from_json

input_file_name = sys.argv[1]
print("TEST_HERE")
print(input_file_name)

conf = SparkConf().setAppName("Jack").setMaster("local").set('spark.driver.memory', '6G').set('spark.driver.maxResultSize', '10G')
sc = SparkContext.getOrCreate(conf = conf)
spark = SparkSession.builder.appName("Python Spark SQL Example").getOrCreate()
ssc = StreamingContext(sc, batchDuration = 5)

'''
model = Word2VecModel.load(sc, "text8_long.mdl")
#synonyms = model.findSynonyms('team', 10)

#for word, cosine_distance in synonyms:
#    print ("{}: {}".format(word, cosine_distance))
vec = model.transform('good')
print(len(vec))
vec = model.transform('bad')
print(len(vec))
vec = model.transform('smart')
print(len(vec))
'''


#print("TEST")
#train_vec = [[0.0, 0.0, 0.0], [0.1, 0.1, 0.1],[0.2, 0.2, 0.2], [9.0, 9.0, 9.0], [9.1, 9.1, 9.1], [9.2, 9.2, 9.2]]
#train_vec = [
#    Vectors.dense([0.0, 0.0, 0.0]), 
#    Vectors.dense([0.1, 0.1, 0.1]),
#    Vectors.dense([0.2, 0.2, 0.2]), 
#    Vectors.dense([9.0, 9.0, 9.0]), 
#    Vectors.dense([9.1, 9.1, 9.1]), 
#    Vectors.dense([9.2, 9.2, 9.2])]

#train_vec = tweet_vectors()
#train_vec = tweet_vectors_from_json()
train_vec = tweet_vectors_from_json(input_file_name)

print(len(train_vec))


#print(sc.parallelize(train_vec).collect())

# we make an input stream of vectors for training,
# as well as a stream of vectors for testing
def parse(lp):
    label = float(lp[lp.find('(') + 1: lp.find(')')])
    vec = Vectors.dense(lp[lp.find('[') + 1: lp.find(']')].split(','))

    return LabeledPoint(label, vec)

#trainingData = sc.textFile("data/mllib/kmeans_data.txt")\
#trainingData = sc.textFile("kmeans_data.txt").map(lambda line: Vectors.dense([float(x) for x in line.strip().split(' ')]))
trainingData = sc.parallelize(train_vec)


label_ = 0
def parse_vec(vec):
    global label_
    label_ += 1
    return LabeledPoint(label_, vec)


#testingData = sc.textFile("data/mllib/streaming_kmeans_data_test.txt").map(parse)
#testingData = sc.textFile("streaming_kmeans_data_test.txt").map(parse)
testingData = sc.parallelize(train_vec).map(parse_vec)

trainingQueue = [trainingData]
testingQueue = [testingData]

trainingStream = ssc.queueStream(trainingQueue)
testingStream = ssc.queueStream(testingQueue)

# We create a model with random clusters and specify the number of clusters to find
#model = StreamingKMeans(k=2, decayFactor=1.0).setRandomCenters(3, 1.0, 0)
model = StreamingKMeans(k=3, decayFactor=1.0).setRandomCenters(100, 1.0, 0)

# Now register the streams for training and testing and start the job,
# printing the predicted cluster assignments on new data points as they arrive.


#model.predictOnValues(testData.map(lp => (lp.label, lp.features))).print()
#model.trainOn(trainingStream)
#print("TEST HERE")
#result = model.predictOnValues(testingStream.map(lambda lp: (lp.label, lp.features)))
model.trainOn(trainingStream)
print("TEST HERE")
result = model.predictOnValues(testingStream.map(lambda lp: (lp.label, lp.features)))
#result.pprint(num = 20)

#if result.count() != 0:
#result.saveAsTextFiles('out2/test_out')
result.saveAsTextFiles('out3/test_out')

#print(result)
ssc.start()
ssc.awaitTerminationOrTimeout(100)
#ssc.stop()
#ssc.stop(stopSparkContext=True, stopGraceFully=True)
#ssc.awaitTermination()
#ssc.stop(stopSparkContext=True, stopGraceFully=True)
#ssc.awaitTerminationOrTimeout()

