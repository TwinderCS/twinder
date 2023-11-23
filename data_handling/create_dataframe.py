'''
Program that takes in input the interesting data and adds it to a dataframe.
'''
import pandas as pd
import numpy as np
import sys
import time
sys.path.append('dumps')
sys.path.append('metrics_handlers')
sys.path.append('classifiers')
from cleaner import cleaner
from metrics import *

def get_hashtags(text : str):
    '''
    Take a text in argument, return its #hashtags in a list.
    '''
    tgs = []
    for word in text.split(" "):
        try:
            if word[0] == "#":
                tgs.append(word)
        except ValueError:
            pass
    return tgs

def get_mentions(text):
    '''
    Take a text in argument, return its @mentions in a list.
    '''
    mts = []
    for word in text.split(" "):
        try:
            if word[0] == "@":
                mts.append(word)
        except ValueError:
            pass
    return mts

def polarity(num):
    if num == 0:
        return 'negative'
    elif num == 2:
        return 'neutral'
    elif num == 4:
        return 'positive'

def create_dataframe(location="../dumps/tweets.csv", save=True):
    df = pd.read_csv(location, index_col="ids", usecols=[0,1,2,4,5])
    df['date'] = pd.to_datetime(df['date'], format="%a %b %d %H:%M:%S PDT %Y")
    df['hashtags'] = df['text'].map(get_hashtags)
    df['mentions'] = df['text'].map(get_mentions)
    df['polarity'] = df['polarity'].map(polarity) # transformer 0, 2, 4 en negative, neutral, positive

    if save:
        df.to_pickle("../dumps/df.pkl")
    return df

def create_emotion_dataframe(location = "dumps/emotion.csv", save = True):
    df = pd.read_csv(location)
    tot = len(df['text'])
    df['text'] = df['text'].map(cleaner)
    if save:
        df.to_pickle('dumps/emotion.pkl')
    
def create_basic_dataframe(location, save_location=None, save = True, idx_col=None):
    if not idx_col is None:
        df = pd.read_csv(location)
    else:
        df = pd.read_csv(location, index_col = idx_col)
    if save:
        df.to_pickle(save_location)
    return df

def create_topic_dataframe(location = "dumps/topic.csv", save = True):
    df = pd.read_csv(location)
    tot = len(df['text'])
    df['text'] = df['text'].map(cleaner)
    if save:
        df.to_pickle('dumps/topic.pkl')

def create_tweets_dataframe(location = 'dumps/tweets.csv', save = True):
    df = pd.read_csv(location)
    if save:
        df.to_pickle('dumps/tweets.pkl')

def create_metrics_dataframe(save = True, nb_users = 300):
    df_tweets = pd.read_pickle('dumps/tweets.pkl')
    usernames = np.array(df_tweets['user'].unique())
    data = []
    vfunc = np.vectorize(get_metric_from_user, otypes=[np.ndarray])
    begin = time.time()
    vectors = vfunc(usernames[0:nb_users])
    df_metric = pd.DataFrame({'username' : usernames[:nb_users], 'metric' : vectors})
    end = time.time()
    if save:
        df_metric.to_pickle('dumps/metrics.pkl')
        df_metric.to_csv('dumps/metrics.csv')
    return end - begin
