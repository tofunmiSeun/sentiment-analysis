class Constant:
    DB_CONNECTION_URL = "mongodb://localhost:27017/"
    DB_NAME = "corruption-sentiment-analysis"
    TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE = "Tweet is already saved in the DB"

    POSITIVE_TWEET_OUTPUT_VALUE = 1
    NEGATIVE_TWEET_OUTPUT_VALUE = 2
    NEUTRAL_TWEET_OUTPUT_VALUE = 0
