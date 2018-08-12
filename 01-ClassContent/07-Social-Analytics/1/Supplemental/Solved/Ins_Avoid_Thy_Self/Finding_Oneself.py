# Dependencies
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Target Term
target_term = "SouthwestAir"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Search for all tweets
public_tweets = api.search(target_term, count=5, result_type="recent")

# Loop through all public_tweets
for tweet in public_tweets["statuses"]:

    # Get ID and Author of most recent tweet directed to me
    tweet_id = tweet["id"]
    tweet_author = tweet["user"]["screen_name"]
    tweet_text = tweet["text"]

    # Print Tweet Text and Tweet Author
    print(tweet_text)
    print(tweet_author)
