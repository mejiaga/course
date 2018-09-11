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

# Create variable for holding the oldest tweet
oldest_tweet = ""

# Loop through 5 times (total of 500 tweets)
for x in range(5):

    # Retrieve 100 most recent tweets -- specifying a max_id
    public_tweets = api.search(
        search_term,
        count=100,
        result_type="recent",
        max_id=oldest_tweet)

    # Print Tweets
    for tweet in public_tweets["statuses"]:

        # Use filters to check if user meets conditions
        if (tweet["user"]["followers_count"] < max_followers and
            tweet["user"]["statuses_count"] > min_tweets and
            tweet["user"]["statuses_count"] < max_tweets and
            tweet["user"]["friends_count"] < max_following and
                tweet["user"]["lang"] == lang):

            # Utilize JSON dumps to generate a pretty-printed json
            # print(json.dumps(
            #     tweet, sort_keys=True, indent=4, separators=(',', ': ')))

            # Add tweets to the tweet array
            tweet_array.append(tweet)

            # Print the username
            print(tweet["user"]["screen_name"])

            # Print the tweet id
            print(tweet["id_str"])

            # Print the tweet text
            print(tweet["text"].encode("UTF-8"))
            print("")

        # Reassign the the oldest tweet (i.e. the max_id)
        oldest_tweet = tweet["id_str"]

# Print total number of tweets
print(len(tweet_array))
