
"""To have the text_analysis and the databases"""
import sys
sys.path.append('text_analysis')
sys.path.append('dumps')
sys.path.append('data_handling')
#from models import *
import time
import numpy as np
from text_analysis import *
import pandas as pd

max_len = 280
emotions = ["joy", "sadness", "fear", "anger", "surprise", "neutral", "shame", "disgust"]
polarity = ['negative', 'neutral', 'positive']
topics = ["politics", "health", "emotion", "financial", "sport", "science"]
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
df = pd.read_csv('dumps/tweets.csv')

def topic_to_vector(topic : str):
    """
    Same function as before for the topics
    """
    for i in range(len(topics)):
        if topic == topics[i]:
            arg = i
    topic_vector = np.zeros(len(topics))
    topic_vector[arg] = 1
    return topic_vector    

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
    emotion = 'joy' #emotion_model(tweet)
    topic = 'politics' #topic_model(tweet)
    polarity = cl.classify(tweet)

    emotion_vector = emotion_dict[emotion]
    topic_vector = topic_to_vector(topic)
    pol_vector = polarity_dict[polarity]

    mind_state_vector = alpha * pol_vector + (1-alpha) * emotion_vector
    metrics = np.concatenate((mind_state_vector, topic_vector))
    return metrics

def get_metric_from_user(user : str, df = df):
    """
    Iterates over all of the user's tweets to return the average of get_metric_from_tweet
    """
    
    begin = time.time()
    user_tweets_df = df[df['user'] == user]
    #print(user_tweets_df.head(8))
    nb_tweets = 0
    user_metric = np.zeros(14, dtype=float)
    for tweet in user_tweets_df['text']:
        nb_tweets += 1
        user_metric += get_metric_from_tweet(tweet)
    mean_vector = user_metric/nb_tweets
    end = time.time()
    print(end-begin)
    return mean_vector
    #print(user_metric/nb_tweets)

def distance(v1, v2):
    """Returns the euclidian distance of v1 and v2"""
    if len(v1) != len(v2):
        print("Error distance : vectors with different sizes")
    if len(v1) == 0:
        print("Error distance : empty vector")

    return np.sum([(v1[i] - v2[i])**2 for i in range(len(v1))])**(0.5)

def get_closest_users(username, n = 10, N = 100):
    """
    Will only consider the first N users 
    Go throught the users and calculate the distances to the user's vector
    and returns the n closest
    """

    df_metric = pd.read_pickle("dumps/metrics.pkl")
    #print(df.head(10))
     
    metric = df_metric[df_metric['username'] == username]['metric'].iloc[0]
    
    """Les 10 premiers users différents de celui donné en arg"""
    users_with_metric = list(df_metric[df_metric['username'] != username][['username', 'metric']].itertuples(index=False, name=None))
    

    user_with_dist = np.array([[distance(metric, user_metric), username] for (username, user_metric) in users_with_metric[0:N]])
    print(len(user_with_dist))

    closest_arg = np.argpartition(user_with_dist, n, axis = 0)[:,0][:n]

    closest_users = user_with_dist[closest_arg, 1]

    return closest_users

