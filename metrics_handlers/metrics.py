
"""

To config the metrics database and to modify the metric's config, with
the different classifiers and models

No need to run this otherwise.

"""



import sys
sys.path.append('classifiers')
sys.path.append('dumps')
sys.path.append('data_handling')
sys.path.append('metrics_handlers')
from models import *
import numpy as np
from textblob_classifier import get_classifier
import pandas as pd
from metrics_fetcher import *
from models import *


polarity = ['negative', 'neutral', 'positive']
alpha = 0.7

#Having dictionnaries is faster than implementing functions (only created once)

"""Gives the emotion vector, going from quite positive to quite negative"""
emotion_dict = {'joy' : np.array([1, 0, 0, 0, 0, 0, 0, 0], dtype = float),
                'surprise' : np.array([0, 1, 0, 0, 0, 0, 0, 0], dtype = float),
                'neutral' : np.array([0, 0, 1, 0, 0, 0, 0, 0], dtype = float),
                'fear' : np.array([0, 0, 0, 1, 0, 0, 0, 0], dtype = float),
                'anger' : np.array([0, 0, 0, 0, 1, 0, 0, 0], dtype = float),
                'shame' : np.array([0, 0, 0, 0, 0, 1, 0, 0], dtype = float),
                'disgust' : np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype = float),
                'sadness' : np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype = float)}

"""
    Associates each polarity (positive, neutral, negative) to several emotions
    to later balance the outputs of the classifier and the emotion network (same size arrays)
"""
polarity_dict = {'positive' : np.array([1, 1, 0, 0, 0, 0, 0, 0], dtype = float),
                 'neutral' : np.array([0, 0, 1, 0, 0, 0, 0, 0], dtype = float),
                 'negative' : np.array([0, 0, 0, 1, 1, 1, 1, 1], dtype = float)}
"""
topic_dict has for each topic a numpy array with only a 1 at the index of the topic in topics
"""
topic_dict = {topics[i] : np.array([0] * i + [1] + (len(topics)-i - 1) * [0], dtype = float) for i in range(len(topics))}


cl = get_classifier()
df_tweets = pd.read_csv('dumps/tweets.csv')

def get_metric_from_tweet(tweet : str, alpha = alpha, cl = cl):
    """
    Returns the vector that represents the tweets thanks to the classifier and the 2 networks
    Because the emotions handler network as a quite low accuracy due to the database (60 %), 
    we use the classifier (which only returns positive, neutral or negative with better accuracy) to help.

    Each emotion as been associated with a polarity (polarity_dict),
    and we create the mind_state_vector with a barycenter of the polarity and the emotion_vector, 

    mind_state_vector = alpha * polarity_vector + (1-alpha) * emotion_vector
    with alpha between 0.5 and 1 (more power to the polarity)
    """
    emotion = emotion_model(tweet)
    topic = topic_model(tweet)
    polarity = cl.classify(tweet)

    emotion_vector = emotion_dict[emotion]
    topic_vector = topic_dict[topic]
    pol_vector = polarity_dict[polarity]

    mind_state_vector = alpha * pol_vector + (1-alpha) * emotion_vector
    metrics = np.concatenate((mind_state_vector, topic_vector))
    return metrics

def get_metric_from_user(user : str, df = df_tweets, debug = False):
    """
    Iterates over all of the user's tweets to return the average of get_metric_from_tweet
    """
    user_tweets_df = df[df['user'] == user]
    if debug:
        print(user_tweets_df.head(8))
    nb_tweets = 0
    user_metric = np.zeros(14, dtype=float)
    for tweet in user_tweets_df['text']:
        nb_tweets += 1
        user_metric += get_metric_from_tweet(tweet)
    mean_vector = user_metric/nb_tweets
    return mean_vector
    if debug:
        print(user_metric/nb_tweets)
