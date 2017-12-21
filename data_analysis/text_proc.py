import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import reprlib

import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'


def clean_text(tweet):
    #print(word_tokenize(tweet))
    #print(preprocess(tweet))
    #return tweet
    return preprocess(tweet)


'''

def clean_text(tweet):
    raw_docs = tweet
    # Tokenizing text into bags of words
    import nltk
    from nltk.tokenize import word_tokenize
    tokenized_docs = [word_tokenize(doc) for doc in raw_docs]

    # Removing punctuation
    import re
    import string
    regex = re.compile('[%s]' % re.escape(string.punctuation))

    tokenized_docs_no_punctuation = []

    for review in tokenized_docs:
        new_review = []
        for token in review:
            new_token = regex.sub(u'', token)
            if not new_token == u'':
                new_review.append(new_token)
    
        tokenized_docs_no_punctuation.append(new_review)


    #return tokenized_docs_no_punctuation
    from nltk.corpus import stopwords

    tokenized_docs_no_stopwords = []

    for doc in tokenized_docs_no_punctuation:
        new_term_vector = []
        for word in doc:
            if not word in stopwords.words('english'):
                new_term_vector.append(word)
    
        tokenized_docs_no_stopwords.append(new_term_vector)

    from nltk.stem.porter import PorterStemmer
    from nltk.stem.snowball import SnowballStemmer
    from nltk.stem.wordnet import WordNetLemmatizer

    porter = PorterStemmer()
    snowball = SnowballStemmer('english')
    wordnet = WordNetLemmatizer()

    preprocessed_docs = []

    for doc in tokenized_docs_no_stopwords:
        final_doc = []
        for word in doc:
            final_doc.append(porter.stem(word))
            
        preprocessed_docs.append(final_doc)

    clean_text = ''
    for i in range(len(preprocessed_docs)):
        for j in range(len(preprocessed_docs[i])):
            clean_text += preprocessed_docs[i][j]
            clean_text += ' '

    return clean_text
'''

if __name__ == "__main__":
    filename = 'all_tweets_text.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    cnt = 1
    for line in lines:
        print ("COUNT " + str(cnt))
        print (line)
        c_line = clean_text(line)
        print("C_LINE")
        print (c_line)
        cnt += 1

    #ct = clean_text(filename)
    #print(ct)

    #text = ct
    #vectorizer = CountVectorizer()
    #text = vectorizer.fit_transform(text)
    #transformer = TfidfTransformer()
