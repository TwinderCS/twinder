from tweet_collection.collection import TweetCollector

collector = TweetCollector()
tweets = collector.search_collect("Emmanuel Macron")
statuses = collector.user_collect("@elonmusk")
print("Tweets")
for tweet in tweets:
    print(tweet.text)
print("Statuses")
for status in statuses:
    print(status.text)
