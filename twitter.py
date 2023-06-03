import tweepy
import time

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_id = "YOUR_TWEET_ID"
custom_message = "Ceci est un retweet avec un message personnalisé !"

while True:
    api.update_status(f"{custom_message} \n\n{tweet_id}")
    print("Le tweet a été retweeté avec succès.")
    time.sleep(60)
