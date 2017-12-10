from pymongo import MongoClient
from Constants import Constant


class TweetsDB:

    COLLECTION_NAME = "relevantTweets"

    @staticmethod
    def save_tweet(new_tweet):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][TweetsDB.COLLECTION_NAME]

            if document.find_one({"tweet_id": new_tweet.id_str}) is not None:
                raise Exception(Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE)

            obj = {
                "tweet_id": new_tweet.id_str,
                "tweet": new_tweet.text
            }

            document.insert(obj)
            client.close()

        except Exception as e:
            print('unable to save new tweet to DB: ' + str(e))

            if str(e) == Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE:
                raise Exception(Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE)

            raise Exception('Could not add new tweet to DB')
