import tweepy
from database.tweetsDB import TweetsDB
from data_scraping.MyStreamListener import MyStreamListener


class TwitterScraper:
    TWITTER_CREDENTIALS_FILE_NAME = "data_scraping/credentials"
    CORRUPTION_KEYWORDS_FILE_NAME = "data_scraping/corruptionKeyWords"

    CREDENTIALS_KEYS = ["CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN_KEY", "ACCESS_TOKEN_SECRET"]
    NIGERIA_GEOCODE_INFROMATION = "9.054362,7.426758,961.12km"

    @staticmethod
    def get_twitter_api():
        credentials_dictionary = {}

        text = open(TwitterScraper.TWITTER_CREDENTIALS_FILE_NAME, "r").read()
        lines = text.split()

        for l in lines:
            arr = l.split("=")
            credentials_dictionary[arr[0]] = arr[1]

        auth = tweepy.OAuthHandler(credentials_dictionary.get("CONSUMER_KEY"),
                                   credentials_dictionary.get("CONSUMER_SECRET"))

        auth.set_access_token(credentials_dictionary.get("ACCESS_TOKEN_KEY"),
                              credentials_dictionary.get("ACCESS_TOKEN_SECRET"))

        api = tweepy.API(auth)
        return api

    @staticmethod
    def get_corruption_keywords_query_filter():
        query = ""
        text = open(TwitterScraper.CORRUPTION_KEYWORDS_FILE_NAME, "r").read()
        lines = text.split()

        if len(lines) == 0:
            return query

        query += lines[0]
        for i in range(1, len(lines)):
            query += " OR " + lines[i]

        return query

    @staticmethod
    def scrape_data():
        api = TwitterScraper.get_twitter_api()
        corruption_keywords_query = TwitterScraper.get_corruption_keywords_query_filter()
        #result = api.search(corruption_keywords_query, geocode=TwitterScraper.NIGERIA_GEOCODE_INFROMATION)

        #for item in result:
        #    print(item.text + "\n")

        #   if item.text.startswith("RT @"):
        #        continue
        #   try:
        #        TweetsDB.save_tweet(item)

        #   except Exception as e:
        #        print(str(e))

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

        myStream.filter(track=[corruption_keywords_query])
