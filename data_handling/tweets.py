from models import emotion_model, topic_model
from metrics import emotions, topics
from data_handling import create_dataframe
import pandas as pd

original = pd.read_csv("dumps/tweets.csv")

def clean(original):
    ...

tweets = clean(original)

for topic in topics:
    tweets[topic] = tweets['text'].map(
        lambda tweet: topic_model(tweet)
    )

for emotion in emotion:
    tweets[emotion] = tweets['text'].map(
        lambda tweet: emotion_model(tweet)
    )

