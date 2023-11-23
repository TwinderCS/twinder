import pickle
from textblob import TextBlob
import nltk
from textblob.classifiers import NaiveBayesClassifier
from autocorrect import Speller
import re
import numpy as np
import pandas as pd

#nltk.download('stopwords')
#nltk.download('wordnet')

def cleaner(text : str):
    """
    Cleans the text by
    - running a spellchecker
    - making the text lowercase
    - removing stopwords
    - removing punctuation
    - lemmatizing
    """
    
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

    with open('dumps/cl_data.obj', 'rb') as file:
        cl = pickle.load(file)
    return cl

def save_classifier(cl):
    """Save the classifier Data"""

    with open('dumps/cl_data.obj', 'wb') as file:
    
        pickle.dump(cl, file)

