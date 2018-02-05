import re
from database.checkedTweetsDB import CheckedTweetsDB

stop_words_file_name = "stopwords.txt"

URL_replacement = "URL"
twitter_user_replacement = "TWITTER_USER"


def process_tweet(tweet):
    tweet = tweet.lower()

    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', URL_replacement, tweet)

    tweet = re.sub('@[^\s]+', twitter_user_replacement, tweet)

    tweet = re.sub('[\s]+', ' ', tweet)

    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    tweet = tweet.strip('\'"')
    return tweet


def get_stop_words():
    stop_words = list()
    stop_words.append(twitter_user_replacement)
    stop_words.append(URL_replacement)

    file = open(stop_words_file_name, 'r')
    line = file.readline()
    while line:
        word = line.strip()
        stop_words.append(word)
        line = file.readline()
    file.close()

    return stop_words


def extract_features(tweet):
    stop_words = get_stop_words()
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


tweets = CheckedTweetsDB.get_all_tweets()

tweets = [t["text"] for t in tweets]

a_list = {}

for t in tweets:
    t = process_tweet(t)
    features = list(set(extract_features(t)))
    print(t)
    print(features)
    print("\n")
    for f in features:
        if a_list.get(f) is None:
            a_list[f] = 1
        else:
            a_list[f] += 1

for key in a_list:
    print(key + ": " + str(a_list[key]))
