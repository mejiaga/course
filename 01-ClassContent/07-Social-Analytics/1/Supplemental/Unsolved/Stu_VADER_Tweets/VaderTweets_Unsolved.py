# Dependencies
import tweepy
import json
import numpy as np

# Import and Initialize Sentiment Analyzer
# YOUR CODE HERE
raise NotImplementedError()

# Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User Account
target_user = "@DalaiLama"

# Variables for holding sentiments
# YOUR CODE HERE
raise NotImplementedError()

# @TODO: UNCOMMENT THE FOLLOWING BLOCK AND COMPLETE THE CODE
#
# # Loop through 10 pages of tweets (total 200 tweets)
# # YOUR CODE HERE
# raise NotImplementedError()


#     # Get all tweets from home feed
#     # YOUR CODE HERE
#     raise NotImplementedError()


#     # Loop through all tweets
#     # YOUR CODE HERE
#     raise NotImplementedError()


#         # Run Vader Analysis on each tweet
#         # YOUR CODE HERE
#         raise NotImplementedError()

#         # Add each value to the appropriate list
#         # YOUR CODE HERE
#         raise NotImplementedError()


# Print the Averages
# YOUR CODE HERE
raise NotImplementedError()
