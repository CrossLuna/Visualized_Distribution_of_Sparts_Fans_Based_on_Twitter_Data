# Visualized Distribution of Sports Fans Based on Twitter Data
EECS 6893 Big Data Analytics

## Prerequisite
1. Python 3.6
2. Spark
3. nltk

## Usage
1. data_fetching: twstream.py can fetch data in real-time. Remember to use your own authentication information. You can also use location and topics information you are interested in.

2. word2vec_training: this part is the code to train the word2vec model. We only train once and load model in latter workflow.

3. data_analysis 
 - text_proc.py: this file includes functions about text cleaning
 - word2vec_test.py: this file includes the routine to vectorize clean text
 - streaming_kmeans.py: this is the main analysis part. It loads all the data and run streaming k-means on data. It outputs the data in distributed system form.

4. data_postprocessing: this part summarize output data and aggregate with original tweets json to provide visualization information

5. visualization: html+javascript code for visualization
