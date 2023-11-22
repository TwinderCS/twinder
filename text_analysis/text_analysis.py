import pickle
from textblob import TextBlob
from nltk.corpus import stopwords
import nltk
from textblob.classifiers import NaiveBayesClassifier
from autocorrect import Speller
import re
import numpy as np



def cleaner(text : str):
    '''cleans the text'''
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
    df = pd.read_pickle("dumps/df.pkl")
    tweets = df['text'].to_numpy()
    polarity = df['polarity'].to_numpy()
    df_all = [(tweets[i], polarity[i]) for i in range(len(tweets))]

    np.random.shuffle(df_all)
    train = df_all[0:1000] #Otherwise it takes wayyy to long
    return NaiveBayesClassifier(train)
    

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

