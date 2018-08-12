# Dependencies
import tweepy
import json

# Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Note: Twitter prevents tweeting the same status or message multiple
# times. Be sure to change the text when testing.

# Create two status updates

# Create a status update with an image

# Create a friendship with another user

# Send a direct message to another user (Hint: You will need them to
# follow your account)

# Bonus: Retweet any tweet from someone else's account (Hint: You will
# need to locate a tweet's id)

# Bonus: Delete your most recent tweet (Hint: "Destroy")

# Bonus: Delete your most recent sent message (Hint: "Destroy")
