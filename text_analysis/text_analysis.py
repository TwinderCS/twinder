import pickle
from textblob import TextBlob
from nltk.corpus import stopwords
import nltk
from text_analysis.classifier_data import *
from textblob.classifiers import NaiveBayesClassifier
from autocorrect import Speller
import re


def cleaner(text):
    speller = Speller(lang='en')
    unpunctuated = re.sub("[^a-zA-Z\s]+", " ", text)
    lowered = unpunctuated.lower()
    text = lowered
    stops = nltk.corpus.stopwords.words('english')
    words = [word for word in text.split(" ") if word not in stops]
    corrected = [speller(word) for word in words]
    lm = nltk.stem.WordNetLemmatizer()
    lemmatized = [lm.lemmatize(word) for word in corrected]
    return " ".join(lemmatized)


def get_new_classifier():
    """Creates a new classifier from scratch"""
    cl = NaiveBayesClassifier(TRAIN_FROM_DF)
    return cl

def get_classifier():
    """Gets the trained classifier from the file"""
    with open('text_analysis/cl_data.obj', 'rb') as file:
        cl = pickle.load(file)
    return cl

def save_classifier(cl):
    """Save the classifier Data"""
    with open('text_analysis/cl_data.obj', 'wb') as file:
    #file = open('text_analysis/cl_data.obj', 'wb')
        pickle.dump(cl, file)
    #file.close()

def get_lemmas_from_tweets(tweets):
    """Returns the lemmas for each words in each tweet of tweets : 
    example : octopi are blue -> octupus is blue"""
    ret = []
    for tweet in tweets:
        tx_blob_tweet = TextBlob(tweet).correct()
        for word in tx_blob_tweet.words:
            if word not in stopwords.words('english'):
                ret.append(word.lemmatize())
    ret = list(set(ret))
    return ret

def get_opinion_rate(tweets):
    """gives the average of positive, neutral, negative tweets
        thanks to the classifier"""
    pos_rate, neu_rate, neg_rate = 0, 0, 0
    for tweet in tweets:
        #cl = get_new_classifier()
        classified = cl.classify(tweet)
        if classified == 'positive':
            pos_rate += 1
        elif classified == 'neutral':
            neu_rate += 1
        else:
            neg_rate +=1
    return (pos_rate/len(tweets), neu_rate/len(tweets), neg_rate/len(tweets))

cl = get_new_classifier()
print(get_opinion_rate(['this is cool'], cl))
print(cl.accuracy(TRAIN_FROM_DF_ALL[2000::]))