# Dependencies
import tweepy
import json

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Search Term
search_term = input("Which term would you like to search for? ")

# Search for all tweets
public_tweets = api.search(search_term, rpp=10)

# View Search Object
# print(public_tweets)

# Loop through all tweets
for tweet in public_tweets["statuses"]:

    # Utilize JSON dumps to generate a pretty-printed json
    # print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': ')))
    print(tweet["text"])
