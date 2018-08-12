# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Weather API
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"

# Target Term
target_term = "@DaDataBootcamp"


# Create a function that checks for tweets sent to the account,
# parses for hashtags, then responds with the weather.
def WeatherTweet():

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Create a variable for storing the requested hashtag
    hashtag = ""

    # Search for most recent tweet directed to the account
    public_tweets = api.search(target_term, count=1, result_type="recent")

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

        # Loop through all hashtags and print each one included
        for hashtag in tweet["entities"]["hashtags"]:

            # Store the hashtag
            hashtag = hashtag["text"]

            # Print the hashtag for display
            print(hashtag)

    # Utilize the hashtag to construct a Query URL for the OpenWeatherMap

    url = "http://api.openweathermap.org/data/2.5/weather?"
    # city = hashtag
    city = "Long Beach Island"
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Tweet the weather
    api.update_status(
        "%s weather as of %s: %s F" %
        (hashtag,
         datetime.datetime.now().strftime("%I:%M %p"),
         weather_json["main"]["temp"]))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every 1 minute
while(True):
    WeatherTweet()
    time.sleep(60)
