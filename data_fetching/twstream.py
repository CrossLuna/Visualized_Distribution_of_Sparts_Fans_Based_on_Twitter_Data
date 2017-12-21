import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Authentication 

consumer_key = "[YOUR CONSUMER KEY]"  
consumer_secret = "[YOUR CONSUMER SECRET]"  
access_token = "[YOUR_ACCESS_TOKEN]"  
access_token_secret = "[YOUR_ACCESS_TOKEN_SECRET]" 

top = 49.3457868 # north lat
left = -124.7844079 # west long
right = -66.9513812 # east long
bottom = 24.7433195 # south lat
# Geographic location
GEOBOX_NYC = [-74.1687, 40.5722, -73.8062, 40.9467]
GEOBOX_USA = [left, bottom, right, top]
#TAGS = ['NFL', 'NBA', 'MLB']
TAGS = ['NFL', 'NBA', 'MLB', 'baseball', 'football', 'basketball']
allTweets = []

tweetCount = 0
#max_tweet_count = 2
#max_tweet_count = 100
max_tweet_count = 15000
iter_max = 5
iter_num = 0


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_status(self, status):
        #print(status)
        global tweetCount
        global allTweets
        print('Status')
        print(tweetCount)
        tweetCount += 1
        allTweets.append(status)
        if tweetCount >= max_tweet_count:
            return False
        return True
    
    '''
    def on_data(self, data):
        #print (data)
        
        #print("Data")
        #print(data)
        #return True
        
        global tweetCount
        global allTweets
        print('Status')
        print(tweetCount)
        tweetCount += 1
        allTweets.append(data)
        print(data)
        if tweetCount >= max_tweet_count:
            return False
        return True
    '''

    def on_error(self, status):
        print ("Error Status")
        print (status)

def dump_all_tweets_text(allTweets, fileName = 'all_tweets_text.txt'):
    file = open(fileName, 'w') 
    print ("Writing tweet objects to JSON text please wait...")
    for status in allTweets:
        #json.dump(status._json, file, sort_keys = True, indent = 4)
        #file.write(json)
        #js_obj = json.loads(status._json)
        js_obj = status._json
        #print(js_obj['text'])
        file.write(js_obj['text'] + '\n')
        #print(js_obj['text'])
    file.close()


def dump_all_tweets(allTweets, fileName = 'all_tweets.json'):
    file = open(fileName, 'w') 
    print ("Writing tweet objects to JSON please wait...")
    for status in allTweets:
        json.dump(status._json, file, sort_keys = True, indent = 4)
    file.close()

def dump_all_tweets_list(allTweets, fileName = 'all_tweets_list.json'):
    global iter_max
    global iter_num
    file = open(fileName, 'w') 
    print ("Writing tweet objects to JSON please wait...")
    cnt = 1;
    file.write('[')
    for status in allTweets:
        json.dump(status._json, file, sort_keys = True, indent = 4)
        if cnt < len(allTweets):
            file.write(',')
            cnt += 1
            iter_num += 1
            #if iter_num > iter_max:
            #    file.close()
            #    file.open(fileName, 'a')
            #    iter_num = 0
    file.write(']')
    file.close()

if __name__ == '__main__':
    tweetCount = 0
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    #stream.filter(locations = GEOBOX_NYC, track=TAGS, languages=["en"])
    stream.filter(locations = GEOBOX_USA, track=TAGS, languages=["en"])

    print (len(allTweets))
    #dump_all_tweets_text(allTweets)
    #dump_all_tweets_list(allTweets)
    dump_all_tweets_list(allTweets, 'all_tweets_list16.json')
    #dump_all_tweets(allTweets)

