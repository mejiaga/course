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

# "Real Person" Filters
min_tweets = 5
max_tweets = 10000
max_followers = 2500
max_following = 2500
lang = "en"

# Search for People Tweeting about Katy Perry
search_term = "Katy Perry"

# Array of Eligible Tweets
tweet_array = []

# Retrieve 100 tweets
public_tweets = api.search(search_term, count=100)

# Print Tweets
for tweet in public_tweets["statuses"]:

    # Utilize JSON dumps to generate a pretty-printed json
    # print(json.dumps(
    #     tweet, sort_keys=True, indent=4, separators=(',', ': ')))

    # Use filters to check if user meets conditions
    if (tweet["user"]["followers_count"] < max_followers and
        tweet["user"]["statuses_count"] > min_tweets and
        tweet["user"]["statuses_count"] < max_tweets and
        tweet["user"]["friends_count"] < max_following and
            tweet["user"]["lang"] == lang):

        # If so add the user's tweet to the array (for future use)
        tweet_array.append(tweet["text"])

        # Print the username
        print(tweet["user"]["screen_name"])

        # Print the tweet text
        print(tweet["text"].encode("UTF-8"))
        print("")

# Print total number of tweets
print(len(tweet_array))
