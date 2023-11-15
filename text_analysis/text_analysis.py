import pandas as pd
from pandas import DataFrame
from textblob import TextBlob, Word
from nltk.corpus import stopwords
from classifier_data import *
from textblob.classifiers import NaiveBayesClassifier


#train du classifier
cl = NaiveBayesClassifier(train) #NaiveBayesClassifier(train_from_df)
df = pd.read_pickle("dumps/df.pkl")

#wiki = TextBlob("I hated that guys octopi")


def get_lemmas_from_tweets(tweets):
    ret = []
    for tweet in tweets:
        tB_tweet = TextBlob(tweet).correct()
        for word in tB_tweet.words:
            if word not in stopwords.words('english'):
                ret.append(word.lemmatize())
    ret = list(set(ret))
    return ret

def get_opinion_rate(tweets):
    pos_rate, neu_rate, neg_rate = 0, 0, 0
    for tweet in tweets:
        classified = cl.classify(tweet)
        if classified == 'pos' or classified == 'positive':
            pos_rate += 1
        elif classified == 'neu' or classified == 'neutral':
            neu_rate += 1
        else:
            neg_rate +=1
    return (pos_rate/len(tweets), neu_rate/len(tweets), neg_rate/len(tweets))


print(get_opinion_rate(["This is cool !"]))
#print(df.iloc[[0, 99], [0, 3]])
#print(cl.classify("This is cool"))
#print(getLemmasFromTweets(['octopi are cool creatures', 'guys and girls']))
#print(TextBlob("This is cool").classify())
