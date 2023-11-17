

"""To have the text_analysis"""
import sys
sys.path.append('text_analysis')
sys.path.append('dumps')
sys.path.append('data_handling')
#from models import *
import numpy as np
from text_analysis import *
import pandas as pd

max_len = 280
emotions = ["joy", "sadness", "fear", "anger", "surprise", "neutral", "shame", "disgust"]
polarity = ['negative', 'neutral', 'positive']
topics = ["politics", "health", "emotion", "financial", "sport", "science"]
alpha = 0.7

def emotion_to_vector(emotion : str):
    match emotion:
        case 'joy':
            return np.array([1, 0, 0, 0, 0, 0, 0, 0], dtype = float)
        case 'surprise':
            return np.array([0, 1, 0, 0, 0, 0, 0, 0], dtype = float)
        case 'neutral':
            return np.array([0, 0, 1, 0, 0, 0, 0, 0], dtype = float)
        case 'fear':
            return np.array([0, 0, 0, 1, 0, 0, 0, 0], dtype = float)
        case 'anger':
            return np.array([0, 0, 0, 0, 1, 0, 0, 0], dtype = float)
        case 'shame':
            return np.array([0, 0, 0, 0, 0, 1, 0, 0], dtype = float)
        case 'disgust':
            return np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype = float)
        case "sadness":
            return np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype = float)
    return "Warning: emotion_to_vector : wrong emotion"

def topic_to_vector(topic : str):
    for i in range(len(topics)):
        if topic == topics[i]:
            arg = i
    topic_vector = np.zeros(len(topics))
    topic_vector[arg] = 1
    return topic_vector

def polarity_to_vector(polarity : str):
    match polarity:
        case "positive":
            return np.array([1, 1, 0, 0, 0, 0, 0, 0], dtype = float)
        case "neutral":
            return np.array([0, 0, 1, 0, 0, 0, 0, 0], dtype = float)
        case "negative":
            return np.array([0, 0, 0, 1, 1, 1, 1, 1], dtype = float)
    return "Warning : polarity_to_vector : wrong polarity"
    return topic_vector

def get_metric_from_tweet(tweet : str, alpha = alpha, cl = get_classifier()):

    emotion = 'joy' #emotion_model(tweet)
    topic = 'politics' #topic_model(tweet)
    polarity = cl.classify(tweet)

    emotion_vector = emotion_to_vector(emotion)
    topic_vector = topic_to_vector(topic)
    pol_vector = polarity_to_vector(polarity)

    mind_state_vector = alpha * pol_vector + (1-alpha) * emotion_vector
    metrics = np.concatenate((mind_state_vector, topic_vector))
    return metrics
    #print(polarity_to_vector(pol)

def get_metric_from_user(user : str):
    df = pd.read_csv('dumps/tweets.csv')
    user_tweets_df = df[df['user'] == user]
    #print(user_tweets_df.head(8))
    nb_tweets = 0
    user_metric = np.zeros(14, dtype=float)
    for tweet in user_tweets_df['text']:
        nb_tweets += 1
        user_metric += get_metric_from_tweet(tweet)
    #print(user_metric/nb_tweets)

#get_metric_from_tweet("this is cool")
#print(emotion_to_vector('fear'))
#print(topic_to_vector("politics"))
#get_metric_from_user('scotthamilton')