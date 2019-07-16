import tweepy
from textblob import TextBlob
import csv


consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('modi')

with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Tweet', 'Sentiment'])

    for tweet in public_tweets:

        analysis = TextBlob(tweet.text)
        sentiment = 'Positive' if analysis.sentiment.polarity > 0 else "Negative"
        writer.writerow([tweet.text, sentiment])
