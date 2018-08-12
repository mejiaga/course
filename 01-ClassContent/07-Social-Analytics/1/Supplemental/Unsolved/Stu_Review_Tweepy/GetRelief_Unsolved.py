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

# Target User Account
target_user = "@Stress_tips123"

# Counter
counter = 1

# @TODO: UNCOMMENT THE FOLLOWING BLOCK AND COMPLETE THE CODE
# # Loop through 5 pages of tweets (total 100 tweets)
# for x in range(5):

#     # Get all tweets from home feed
#     # YOUR CODE HERE
#     raise NotImplementedError()

#     # Loop through all tweets
#     for tweet in public_tweets:

#         # Utilize JSON dumps to generate a pretty-printed json
#         # print(json.dumps(
#         #     tweet, sort_keys=True, indent=4, separators=(',', ': ')))

#         # Print Tweets
#         # YOUR CODE HERE
#         raise NotImplementedError()

#         # Add to Counter
#         # YOUR CODE HERE
#         raise NotImplementedError()
