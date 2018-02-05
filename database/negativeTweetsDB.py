from pymongo import MongoClient
from Constants import Constant


class NegativeTweetsDB:
    COLLECTION_NAME = "negativeTweets"

    @staticmethod
    def get_all_tweets():
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][NegativeTweetsDB.COLLECTION_NAME]

            all_tweets = []

            tweets = document.find({})

            for tweet in tweets:
                all_tweets.append({
                    "tweet_id": tweet["tweet_id"],
                    "text": tweet["tweet"]
                })

            client.close()
            return all_tweets

        except Exception as e:
            print('unable to save new tweet to DB: ' + str(e))

            if str(e) == Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE:
                raise Exception(Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE)

            raise Exception('Could not add new tweet to DB')

    @staticmethod
    def save_tweet(new_tweet):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][NegativeTweetsDB.COLLECTION_NAME]

            if document.find_one({"tweet_id": new_tweet["tweet_id"]}) is not None:
                raise Exception(Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE)

            obj = {
                "tweet_id": new_tweet["tweet_id"],
                "tweet": new_tweet["text"]
            }

            document.insert(obj)
            client.close()

        except Exception as e:
            print('unable to save new tweet to DB: ' + str(e))

            if str(e) == Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE:
                raise Exception(Constant.TWEET_ALREADY_EXISTS_EXCEPTION_MESSAGE)

            raise Exception('Could not add new tweet to DB')

    @staticmethod
    def delete_tweet(tweet_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][NegativeTweetsDB.COLLECTION_NAME]

            document.delete_one({"tweet_id": tweet_id})
            client.close()

        except Exception as e:
            print('unable to delete tweet from DB: ' + str(e))