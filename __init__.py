import tweet_visualization
#import wordcloud
import text_analysis
import data_handling
import tests
import metrics_handlers
import pandas as pd


# Lets present various functionalities

## Data Handling
df = data_handling.create_dataframe("dumps/tweets.csv", save=False)
print(df)

## Wordcloud
word_frequencies = wordcloud.word_freq(df['text'])
img = wordcloud.create_image(word_frequencies)
wordcloud.show_wordcloud(img)

## Text Analysis
cl = text_analysis.get_classifier()
print("Opinion Rate:", text_analysis.get_opinion_rate(df['text']))
print("Example:")
print("I love Ice Cream!", cl("I Love Ice Cream!"))
print("I hate Death!", cl("I hate Death!"))
