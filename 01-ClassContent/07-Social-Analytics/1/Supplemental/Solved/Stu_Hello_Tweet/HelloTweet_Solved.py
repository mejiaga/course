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

# Note: Twitter prevents from tweeting the same status or message multiple
# times. Be sure to change the text when testing.

# Create two status updates
api.update_status("Hello There!")
api.update_status("It's a great day!")

# Create a status update with an image
api.update_with_media("get_money.jpg", "Programming skills == ")

# Create a friendship with another user
api.create_friendship(screen_name="@PlotBot5", follow=True)

# Send a direct message to another user (Hint: You will need them to
# follow your account)
api.send_direct_message(user="plotbot5", text="hiiiiiii!!!!!!")

# Bonus: Retweet any tweet from someone else's account (Hint: You will
# need to locate a tweet's id)
target_user = "@ddjournalism"
public_tweets = api.user_timeline(target_user)
tweet_id = public_tweets[0]["id"]
api.retweet(tweet_id)

# Bonus: Delete your most recent tweet (Hint: "Destroy")
my_tweets = api.user_timeline()
tweet_id = my_tweets[0]["id"]
api.destroy_status(tweet_id)

# Bonus: Delete your most recent sent message (Hint: "Destroy")
my_messages = api.sent_direct_messages()
message_id = my_messages[0]["id"]
api.destroy_direct_message(message_id)
