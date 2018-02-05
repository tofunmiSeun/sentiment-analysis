import tweepy
from database.tweetsDB import TweetsDB


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print(tweet.text + "\n")

        if tweet.text.startswith("RT @"):
            return
        try:
            TweetsDB.save_tweet(tweet)

        except Exception as e:
            print(str(e))

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
