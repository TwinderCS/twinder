

"""To have the text_analysis"""
import sys
sys.path.append('text_analysis')
#from models import *
import numpy as np
from text_analysis import *

max_len = 280
emotions = ["joy", "sadness", "fear", "anger", "surprise"]
polarity = ['negative', 'neutral', 'positive']
topics = ["politics", "health", "emotion", "financial", "sport", "science"]


def emotion_to_vector(emotion):
    match emotion:
        case 'joy':
            return np.array([1, 0, 0, 0, 0])
        case 'surprise':
            return np.array([0, 1, 0, 0, 0])
        case 'anger':
            return np.array([0, 0, 1, 0, 0])
        case 'fear':
            return np.array([0, 0, 0, 1, 0])
        case 'anger':
            return np.array([0, 0, 0, 0, 1])
    return "Warning: emotion_to_vector : wrong emotion"

def topic_to_vector(topic):
    for i in range(len(topics)):
        if topic == topics[i]:
            arg = i
    topic_vector = np.zeros(len(topics))
    topic_vector[arg] = 1

    return topic_vector
def get_metrics_from_tweet(tweet):
    emotion = emotion_model(tweet)
    topic = topic_model(tweet)
    cl = get_classifier()
    print(cl.classify(tweet))
#get_metrics_from_tweet("this is cool")
#print(emotion_to_vector('fear'))
#print(topic_to_vector("politics"))