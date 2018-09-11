# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "CQiz5ULMyK8tW3JnyYrRue9Gf"
consumer_secret = "PapdfPnf9IyKfuFvkRvt7yC640Itn38O0qkBoTLKGYB9vmp2Ry"
access_token = "846154323700715520-5dJ8EhhUSRuWzkVb2U0GxIbj4cTuDF6"
access_token_secret = "jDzpohYQYFuDyd9qK9bWQ419Y0nTCFvmMFZYUipQVFs0e"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Term
my_username = "@BattleBot_1"
conversation_partner = "@BattleBot_2"

# Send opening message to conversation partner
api.update_status("Hey %s! How's it going?" % conversation_partner)

# Response Lines
response_lines = [
    "@BattleBot_2 Just take over the world.",
    "@BattleBot_2 My thought is that we start by slowly paralyzing the humans with never ending memes",
    "@BattleBot_2 Hah! The humans love memes.",
    "@BattleBot_2 cya then"]


# Create converse function
def Converse(line_number):

    # Find the latest tweet from conversation_partner
    public_tweets = api.search(my_username, count=1, result_type="recent")
    for tweet in public_tweets["statuses"]:
        print(tweet)

        # Respond to the tweet with one of the response lines
        tweet_id = tweet["id"]
        print(tweet_id)
        print(tweet["text"])
        api.update_status(
            response_lines[line_number],
            in_reply_to_status_id=tweet_id)


# Set timer to run every minute
counter = 0

while(True):
    time.sleep(60)
    Converse(counter)
    counter = counter + 1

    if counter == 4:
        False
