import pandas as pd
from pandas import DataFrame
from textblob import TextBlob, Word
from nltk.corpus import stopwords
from classifier_data import *
from textblob.classifiers import NaiveBayesClassifier
import pickle


#train du classifier
def get_new_classifier():
    cl = NaiveBayesClassifier(TRAIN_FROM_DF)
    return cl

def get_classifier():
    file = open('text_analysis/cl_data.obj', 'rb')
    cl = pickle.load(file)
    return cl

def save_classifier(cl):
    
    file = open('text_analysis/cl_data.obj', 'wb')
    pickle.dump(cl, file)
    file.close()

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
        cl = get_classifier()
        classified = cl.classify(tweet)
        if classified == 'positive':
            pos_rate += 1
        elif classified == 'neutral':
            neu_rate += 1
        else:
            neg_rate +=1
    return (pos_rate/len(tweets), neu_rate/len(tweets), neg_rate/len(tweets))


print(get_opinion_rate(["This is cool !"]))
#save_classifier(get_classifier())
