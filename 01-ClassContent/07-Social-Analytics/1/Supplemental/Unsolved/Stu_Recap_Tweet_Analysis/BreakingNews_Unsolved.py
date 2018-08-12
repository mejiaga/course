# Dependencies
import tweepy
import json
import numpy as np

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Search Term
target_term = "@CNNbrk"

# @TODO: UNCOMMENT THE FOLLOWING BLOCK AND COMPLETE THE CODE
# # Add List to hold sentiment
# # @TODO: YOUR CODE HERE
# raise NotImplementedError()

# # Grab 25 tweets
# # @TODO: YOUR CODE HERE
# raise NotImplementedError()

# # Loop through all tweets
# # @TODO: YOUR CODE HERE
# raise NotImplementedError()

#     # Run Vader Analysis on each tweet
#     # @TODO: YOUR CODE HERE
#     raise NotImplementedError()

#     # Add each value to the appropriate array
#     # @TODO: YOUR CODE HERE
#     raise NotImplementedError()

# # Store the Average Sentiments
# # @TODO: YOUR CODE HERE
# raise NotImplementedError()

# # Print the Sentiments
# # @TODO: YOUR CODE HERE
# raise NotImplementedError()
