import pickle
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import pandas as pd

def get_new_classifier():
    """Creates a new classifier from scratch"""

    df = pd.read_pickle("dumps/df.pkl")
    tweets = df['text'].to_numpy()
    polarity = df['polarity'].to_numpy()
    df_all = [(tweets[i], polarity[i]) for i in range(len(tweets))]

    np.random.shuffle(df_all)
    train = df_all[0:1000] #Otherwise it takes wayyy too long
    return NaiveBayesClassifier(train)


def get_classifier():
    """Gets the trained classifier from the file"""

    with open('dumps/cl_data.obj', 'rb') as file:
        cl = pickle.load(file)
    return cl

def save_classifier(cl):
    """Save the classifier Data"""

    with open('dumps/cl_data.obj', 'wb') as file:
    
        pickle.dump(cl, file)

