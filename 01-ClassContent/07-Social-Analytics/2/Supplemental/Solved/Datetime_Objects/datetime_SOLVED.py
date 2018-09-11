# Dependencies
import tweepy
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User
target_user = 'latimes'

# Get all tweets from home feed
public_tweets = api.user_timeline(target_user)

# A list to hold tweet timestamps
tweet_times = []

# Loop through all tweets
for tweet in public_tweets:
    raw_time = tweet["created_at"]
    # print(raw_time)
    tweet_times.append(raw_time)

# Convert tweet timestamps to datetime objects that can be manipulated by Python
converted_timestamps = []
for raw_time in tweet_times:
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    converted_time = datetime.strptime(raw_time, "%a %b %d %H:%M:%S %z %Y")
    converted_timestamps.append(converted_time)


print(tweet_times[0])
print(tweet_times[1])

print(converted_timestamps[0])
print(converted_timestamps[1])

diff = converted_timestamps[0] - converted_timestamps[1]
print("Time difference: ", diff)
print('seconds: {}'.format(diff.seconds))


converted_length = len(converted_timestamps)
print("length of converted timestamps list: %s" % converted_length)

time_diffs = []

for x in range(converted_length - 1):
    time_diff = converted_timestamps[x] - converted_timestamps[x + 1]
    # print('time diff %s' % time_diff)
    # print('time diff, in seconds %s' % time_diff.seconds)
    # print('time diff, in minutes:', time_diff.seconds/60)
    # print('time diff, hours', time_diff.seconds/3600)

    # convert time_diff to hours
    time_diff = time_diff.seconds / 3600
    time_diffs.append(time_diff)


print("Avg. Hours Between Tweets: %s" % np.mean(time_diffs))
