# Dependencies
import tweepy
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import time

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Specify your twitter account (hint: remember the "@" sign)
my_account = "@DaDataBootcamp"


# Create a function for determining the hashtag included in the most
# recent tweet
def HashtagExtractor():

    # Create a variable for storing the requested hashtag
    hashtag = ""

    # Search for most recent tweet directed to the account
    public_tweets = api.search(my_account, count=1, result_type="recent")

    # Extract hashtag from tweet directed to the account
    for tweet in public_tweets["statuses"]:

        # Print tweet in JSON
        print(
            json.dumps(
                tweet,
                sort_keys=True,
                indent=4,
                separators=(
                    ',',
                    ': ')))

        # Print tweet text
        print(tweet["text"])

        # Grab the first hashtag in the tweet (if one exists)
        try:

            # Loop through all hashtags and print each one included
            for hashtag in tweet["entities"]["hashtags"]:

                # Store the hashtag
                hashtag = hashtag["text"]

                # Print the hashtag for display
                print(hashtag)

                # Return the hashtag for use in the next function
                return hashtag

        # If one does not exist...
        except Exception:            # Print explanation message
            print("No hashtag present")


# Create a function for generating tweet velocity associated with the
# given hashtag
def CreateAndTweetPlot(hashtag):

    # Create array to record all date-times of tweets
    tweet_times = []

    # Get all tweets associated with the hashtag
    public_tweets = api.search(hashtag, count=100, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:

        # Store all tweet times into the array
        tweet_times.append(tweet["created_at"])

        # Print tweets for preview
        print(tweet["created_at"])

    # Convert all tweet times into datetime objects
    tweet_time_objects = []

    # Add each datetime object into the array
    for x in range(len(tweet_times)):
        tweet_datetime = datetime.strptime(
            tweet_times[x], "%a %b %d %H:%M:%S %z %Y")
        tweet_time_objects.append(tweet_datetime)

        # Preview that datetimes are matching
        print(tweet_times[x])
        print(tweet_datetime)

    # Calculate time between tweets
    time_in_between = []

    # Calculate the time in between each tweet
    for x in range(len(tweet_time_objects) - 1):
        mins_apart = (
            (tweet_time_objects[x] - tweet_time_objects[x + 1]).seconds) / 3600
        time_in_between.append(mins_apart)

    # Plot time between tweets
    plt.plot(range(len(time_in_between)), time_in_between, marker="o",
             linewidth=0.25, alpha=0.8, color="r")
    plt.xlim([0, len(time_in_between)])
    plt.ylabel("Hours Apart")
    plt.xlabel("Tweets Ago")
    plt.title("Tweet Velocity: %s" % hashtag)

    # Save the figure
    file_path = "analysis.png"
    plt.savefig(file_path)

    # Print all done
    print("All Done!")

    # Tweet the plot
    # TO DO


# Call the function to run the two functions every minute
while(True):
    hashtag = "#" + HashtagExtractor()
    CreateAndTweetPlot(hashtag)
    time.sleep(60)
