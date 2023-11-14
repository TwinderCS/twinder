import pandas as pd
from pandas import DataFrame
from textblob import TextBlob, Word
from nltk.corpus import stopwords
from classifier_data import DATAFRAME, TRAIN_FROM_DF
from textblob.classifiers import NaiveBayesClassifier


#train du classifier
def get_classifier():
    cl = NaiveBayesClassifier(TRAIN_FROM_DF)

def get_lemmas_from_tweets(tweets):
    ret = []
    for tweet in tweets:
        tB_tweet = TextBlob(tweet).correct()
        for word in tB_tweet.words:
            if word not in stopwords.words('english'):
                ret.append(word.lemmatize())
    ret = list(set(ret))
    return ret

def get_opinion_rate(tweets):
    pos_rate, neu_rate, neg_rate = 0, 0, 0
    for tweet in tweets:
        classified = cl.classify(tweet)
        if classified == 'positive':
            pos_rate += 1
        elif classified == 'neutral':
            neu_rate += 1
        else:
            neg_rate +=1
    return (pos_rate/len(tweets), neu_rate/len(tweets), neg_rate/len(tweets))
