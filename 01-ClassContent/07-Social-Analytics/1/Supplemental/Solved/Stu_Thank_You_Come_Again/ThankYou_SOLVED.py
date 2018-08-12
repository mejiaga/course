# Dependencies
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Target Term
target_term = "@DaDataBootcamp"

# Opening message
print("We're going live, sir!")


# Create Thank You Function
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:

        # Get ID and Author of most recent tweet directed to me
        tweet_id = tweet["id"]
        tweet_author = tweet["user"]["screen_name"]

        # Print the tweet_id
        print(tweet_id)

        # Use Try-Except to avoid the duplicate error
        try:
            # Respond to tweet
            api.update_status(
                "Thank you @%s! Come again!" %
                tweet_author,
                in_reply_to_status_id=tweet_id)

            # Print success message
            print("Successful response, sir!")

        except Exception:
            # Print message if duplicate
            print("Already responded to this one, sir!")

        # Print message to signify complete cycle
        print("We're done for now sir. I'll check again in 60 seconds.")


# Set timer to run every minute
while(True):
    ThankYou()
    time.sleep(60)
