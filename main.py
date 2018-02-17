from database.positiveTweetsDB import PositiveTweetsDB
from database.negativeTweetsDB import NegativeTweetsDB
from database.neutralTweetsDB import NeutralTweetsDB
from data_scraping.tweetProcessor import TweetProccesor
from algorithms.maximumEntropyClassifier import MaximumEntropyClassifier


positive_tweets = PositiveTweetsDB.get_all_tweets()
negative_tweets = NegativeTweetsDB.get_all_tweets()
neutral_tweets = NeutralTweetsDB.get_all_tweets()

trainingInputs = []
trainingOutputs = []

print("POSITIVE TWEETS " + str(len(positive_tweets)))
for tweet in positive_tweets:
    tweet = TweetProccesor.process_tweet(tweet["text"])

    trainingInputs.append(tweet)
    trainingOutputs.append(0)

    print(tweet + "\n")
print()

print("NEGATIVE TWEETS " + str(len(negative_tweets)))
for tweet in negative_tweets:
    tweet = TweetProccesor.process_tweet(tweet["text"])

    trainingInputs.append(tweet)
    trainingOutputs.append(1)

    print(tweet + "\n")
print()

print("NEUTRAL TWEETS " + str(len(neutral_tweets)))
for tweet in neutral_tweets:
    tweet = TweetProccesor.process_tweet(tweet["text"])

    trainingInputs.append(tweet)
    trainingOutputs.append(0)

    print(tweet + "\n")
print()

maxEnt = MaximumEntropyClassifier()
maxEnt.train(trainingInputs, trainingOutputs)

print("done")
