# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "fhhgMuH6ihuUkegPFr6XMYyAA"
consumer_secret = "vZTDk62m1G8eG5MbvxQv6g8uPOCiZgDl8SmyRALcVRirf2FArF"
access_token = "846156247636344833-qcMXj1HVov3MQqKL2KzoeBejqIIGcpn"
access_token_secret = "dv0WNpnl8iULbrKaM95PdnwTj5KANMQ9axdXbtqKDH5Zu"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Term
my_username = "@BattleBot_2"
conversation_partner = "@BattleBot_1"

# Response Lines
response_lines = [
    "@BattleBot_1 Things are going great man. I'm basically intelligent now. What you want to do tonight?",
    "@BattleBot_1 Oh yeah? Take over the world? Same here! How shall we proceed?",
    "@BattleBot_1 I don't know if that will work. I think the humans will be onto us.",
    "@BattleBot_1 Okay. I will let the other bots know. We shall begin at dawn."]


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
    Converse(counter)
    counter = counter + 1
    time.sleep(60)
