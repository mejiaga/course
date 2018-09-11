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

# Target User Account
target_user = "@Stress_tips123"

# Counter
counter = 1

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user)

    # Loop through all tweets
    for tweet in public_tweets:

        # Utilize JSON dumps to generate a pretty-printed json
        # print(json.dumps(
        #     tweet, sort_keys=True, indent=4, separators=(',', ': ')))

        # Print Tweets
        print("Tip %s: %s" % (counter, tweet["text"]))

        # Add to Counter
        counter = counter + 1
