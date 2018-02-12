import re
from database.checkedTweetsDB import CheckedTweetsDB


class TweetProccesor:
    stop_words_file_name = "data_scraping/stopwords.txt"

    URL_replacement = "URL"
    twitter_user_replacement = "TWITTER_USER"

    @staticmethod
    def process_tweet(tweet):
        tweet = tweet.lower()

        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', TweetProccesor.URL_replacement, tweet)

        tweet = re.sub('@[^\s]+', TweetProccesor.twitter_user_replacement, tweet)

        tweet = re.sub('[\s]+', ' ', tweet)

        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

        tweet = tweet.strip('\'"')
        return tweet

    @staticmethod
    def get_stop_words():
        stop_words = list()
        stop_words.append(TweetProccesor.twitter_user_replacement)
        stop_words.append(TweetProccesor.URL_replacement)

        file = open(TweetProccesor.stop_words_file_name, 'r')
        line = file.readline()
        while line:
            word = line.strip()
            stop_words.append(word)
            line = file.readline()
        file.close()

        return stop_words

    @staticmethod
    def extract_features(tweet):
        stop_words = TweetProccesor.get_stop_words()
        features = []

        words = tweet.split()
        for w in words:

            w = w.strip('\'"?,.')

            val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)

            if w in stop_words or val is None:
                continue
            else:
                features.append(w.lower())
        return features
