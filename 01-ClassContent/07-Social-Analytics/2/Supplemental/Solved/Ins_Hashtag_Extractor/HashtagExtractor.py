# Dependencies
import numpy as np
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Term
# target_term = "@DaDataBootCamp"
target_term = "@katyperry"

# Opening message
print("We're going live, sir!")

# Search for most recent tweet directed to the account
public_tweets = api.search(target_term, count=1, result_type="recent")

# Extract all hashtags from tweets directed to the account
for tweet in public_tweets["statuses"]:

    # Print tweet in JSON
    print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': ')))

    # Print tweet text
    print(tweet["text"])

    # Loop through all hashtags and print each one included
    for hashtag in tweet["entities"]["hashtags"]:
        print(hashtag["text"])
