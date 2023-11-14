from pytest import *
from tweet_visualization import *

def test_collect():
    global df
    #tweets = tweet_collect.collect()
    #df =  transform_to_dataframe(tweets)
    assert 'text' in df.columns
test_collect()