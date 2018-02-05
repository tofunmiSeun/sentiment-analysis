class BayesClassifier:
    PROBABILITY_OF_TWEET = 1

    @staticmethod
    def train():
        return list()

    @staticmethod
    def likelihood_of_sentiment(features_to_be_classified, sentiment_training_data, sentiment_probability):
        wordsInSentimentTweets = 0
        for key in sentiment_training_data:
            wordsInSentimentTweets += sentiment_training_data[key]

        likelihood = sentiment_probability / BayesClassifier.PROBABILITY_OF_TWEET

        p_tweet_given_sentiment = 1
        training_data_feature_count = len(sentiment_training_data)

        for feature in features_to_be_classified:
            # Using laplace smoothing to calculate the sentiment probability of each feature
            number_of_occurrence = 1
            frequency_of_feature = sentiment_training_data.get(feature)
            if frequency_of_feature is not None:
                number_of_occurrence += frequency_of_feature
            p_tweet_given_sentiment *= number_of_occurrence / (training_data_feature_count + wordsInSentimentTweets)

        likelihood *= p_tweet_given_sentiment
