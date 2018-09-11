# Dependencies
import json

# Read JSON
sample = "SampleX.json"

# Sample 1 Data
with open(sample) as data_file:
    sample_data = json.load(data_file)

    # Cleaned up JSON
    print(
        json.dumps(
            sample_data[0],
            sort_keys=True,
            indent=4,
            separators=(
                ',',
                ': ')))
    print("------------------------------------------------------------------")

    # Using the Sample_Data provided above, write code to answer each of the
    # following questions:

    # Question 1: What user account is the tweets in the Sample associated
    # with?
    print("User Account: " + sample_data[0]["user"]["name"])
    print("")

    print(sample_data[0]["user"]["name"])

    # Question 2: How many followers does this account have associated with it?
    print(("Follower Count: %s") % (sample_data[0]["user"]["followers_count"]))
    print("")

    # Question 3: How many tweets are included in the Sample?
    print("Tweet Count (In Sample): %s" % (len(sample_data)))
    print("")

    # Question 4: How many tweets total has this account made?
    print("Tweet Count (Total) %s" %
          (sample_data[0]["user"]["statuses_count"]))
    print("")

    # Question 5: What was the text in the most recent tweet? (Hint: You may
    # need to look into "encoding utf-8 in python")
    print("Most Recent Tweet: %s" % (sample_data[0]["text"]))
    print("")

    # Question 6: What was the text associated with each of the tweets
    # included in this sample data?
    print("All Tweets:")
    for tweet in sample_data:
        print("- %s" % (tweet["text"]))
    print("")

    # Question 7 (Bonus): Which of the user's tweets was most frequently
    # retweeted? How many retweets were there?
    top_tweet = ""
    top_tweet_follower_count = 0

    for tweet in sample_data:
        if(tweet["retweet_count"] > top_tweet_follower_count):
            top_tweet = tweet["text"]
            top_tweet_follower_count = tweet["retweet_count"]
    print("Most Popular Tweet: %s" % (top_tweet))
    print("Number of Retweets: %s" % (top_tweet_follower_count))
    print("")
