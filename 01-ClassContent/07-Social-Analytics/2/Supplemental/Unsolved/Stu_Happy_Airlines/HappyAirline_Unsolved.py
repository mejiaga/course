# Dependencies
import tweepy
import json
import numpy as np

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = ""  # Enter your key
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Search Term
target_terms = ("@SouthwestAir", "@AmericanAir", "@SpiritAirlines",
                "@Virginatlantic", "@Delta", "@AlaskaAir", "@KLM")

# "Real Person" Filters
min_tweets = 5
max_tweets = 10000
max_followers = 2500
max_following = 2500
lang = "en"

# Array to hold sentiment
sentiment_array = []

# Variable for holding the oldest tweet
oldest_tweet = ""

# @TODO: UNCOMMENT THE FOLLOWING BLOCK AND COMPLETE THE CODE
#
# # Loop through all target users
# # YOUR CODE HERE
# raise NotImplementedError()

#     # Variables for holding sentiments
#     # YOUR CODE HERE
#     raise NotImplementedError()

#     # Loop through 10 times (total of 1500 tweets)
#     # YOUR CODE HERE
#     raise NotImplementedError()

#         # Run search around each tweet
#         # YOUR CODE HERE
#         raise NotImplementedError()

#         # Loop through all tweets
#         # YOUR CODE HERE
#         raise NotImplementedError()

#             # Use filters to check if user meets conditions
#             # YOUR CODE HERE
#             raise NotImplementedError()

#                 # Run Vader Analysis on each tweet
#                 # YOUR CODE HERE
#                 raise NotImplementedError()

#                 # Add each value to the appropriate array
#                 # YOUR CODE HERE
#                 raise NotImplementedError()

#     # Store the Average Sentiments
#     # YOUR CODE HERE
#     raise NotImplementedError()

#     # Print the Sentiments
#     # YOUR CODE HERE
#     raise NotImplementedError()
