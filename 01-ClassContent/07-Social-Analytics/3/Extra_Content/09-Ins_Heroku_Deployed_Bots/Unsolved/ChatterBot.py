# Dependencies
import tweepy
import time
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create a function that tweets


# Create a function that calls the TweetOut function every minute


# Infinite loop

# Call the TweetQuotes function and specify the tweet number

# Once tweeted, wait 60 seconds before doing anything else

# Add 1 to the counter prior to re-running the loop
