import pandas as pd
from pandas import DataFrame
from textblob import TextBlob
from nltk.corpus import stopwords

#df = pd.read_csv("../dumps/tweets.csv")

wiki = TextBlob("I hated that guys octopi")


def getLemmasFromTweets(tweets):
    ret = []
    for tweet in tweets:
        tB_tweet = TextBlob(tweet)
        for word in tB_tweet.words:
            if word not in stopwords.words('english'):
                ret.append(word.lemmatize())
    ret = list(set(ret))
    return ret

#print(getLemmasFromTweets(['octopi are cool creatures', 'guys and girls']))

"""
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
"""