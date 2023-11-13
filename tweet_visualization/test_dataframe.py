from pytest import *
from tweet_visualization.py import *

def test_collect():
    global df
    #tweets = tweet_collect.collect()
    df =  transform_to_dataframe(tweets)
    assert 'tweet_textual_content' in df.columns
test_collect()