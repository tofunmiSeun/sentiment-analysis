from Constants import Constant


class MaximumEntropyClassifier:
    def __init__(self):
        self.__trained = False
        self.lambdas = None

    def train(self, input_values, output_values):
        if len(input_values) != len(output_values):
            raise Exception("Inconsistent number of input and output training data")

        positive_tweets = {}
        negative_tweets = {}
        neutral_tweets = {}

        word_occurences_dictionary = {}

        N = 0
        Pos = 0
        Neg = 0
        Neu = 0

        for i in range(0, len(input_values)):
            words = input_values[i].split()

            for word in words:
                N += 1

                if word_occurences_dictionary.get(word) is None:
                    word_occurences_dictionary[word] = [0, 0, 0]

                if output_values[i] == Constant.POSITIVE_TWEET_OUTPUT_VALUE:
                    Pos += 1
                    word_occurences_dictionary[word][0] += 1

                    if positive_tweets.get(word) is None:
                        positive_tweets[word] = 1
                    else:
                        positive_tweets[word] += 1

                elif output_values[i] == Constant.NEGATIVE_TWEET_OUTPUT_VALUE:
                    Neg += 1
                    word_occurences_dictionary[word][1] += 1

                    if negative_tweets.get(word) is None:
                        negative_tweets[word] = 1
                    else:
                        negative_tweets[word] += 1

                elif output_values[i] == Constant.NEUTRAL_TWEET_OUTPUT_VALUE:
                    Neu += 1
                    word_occurences_dictionary[word][2] += 1

                    if neutral_tweets.get(word) is None:
                        neutral_tweets[word] = 1
                    else:
                        neutral_tweets[word] += 1
        # To select which words to use as features
        features = MaximumEntropyClassifier.select_features_using_chi_square(word_occurences_dictionary, Pos, Neg, Neu, N, 50)

        # Building feature set for the three types of sentiments
        self.positive_features = [0 for i in range(0, len(features))]
        self.negative_features = [0 for i in range(0, len(features))]
        self.neutral_features = [0 for i in range(0, len(features))]
        self.lambdas = [0 for i in range(0, len(features))]

        for i in range(0, len(features)):
            feature = features[i]

            if positive_tweets.get(feature) is not None:
                self.positive_features[i] += positive_tweets.get(feature)

            if negative_tweets.get(feature) is not None:
                self.negative_features[i] += negative_tweets.get(feature)

            if neutral_tweets.get(feature) is not None:
                self.neutral_features[i] += neutral_tweets.get(feature)

        self.__fit_lambdas()
        self.__trained = True

    def __fit_lambdas(self):
        pass

    @staticmethod
    def select_features_using_chi_square(word_occurrences_dictionary, Pos, Neg, Neu, Total, features_count_limit):

        if features_count_limit < 1:
            raise Exception("You have to have at least one feature")

        for key in word_occurrences_dictionary:
            A = word_occurrences_dictionary[key][0]
            B = word_occurrences_dictionary[key][1]
            C = word_occurrences_dictionary[key][2]

            D = Pos - A
            E = Neg - B
            F = Neu - C

            Ea = (A + B + C) * (A + D) / Total
            Eb = (A + B + C) * (B + E) / Total
            Ec = (A + B + C) * (C + F) / Total
            Ed = (D + E + F) * (A + D) / Total
            Ee = (D + E + F) * (B + E) / Total
            Ef = (D + E + F) * (C + F) / Total

            # chi_square = ((A - Ea) ** 2) / Ea
            chi_square = ((B - Eb) ** 2) / Eb
            chi_square += ((C - Ec) ** 2) / Ec
            # chi_square += ((D - Ed) ** 2) / Ed
            chi_square += ((E - Ee) ** 2) / Ee
            chi_square += ((F - Ef) ** 2) / Ef

            word_occurrences_dictionary[key] = chi_square

        word_occurrences_dictionary = sorted(word_occurrences_dictionary.items(), key=lambda x: x[1])
        word_occurrences_dictionary.reverse()

        features = []
        count = 0
        for word in word_occurrences_dictionary:
            features.append(word[0])
            count += 1
            if count == features_count_limit:
                break

        return features
