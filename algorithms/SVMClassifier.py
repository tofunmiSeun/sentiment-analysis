from sklearn import svm


class SVMClassifier:

    def __init__(self, features_count):
        self.__features_count = features_count
        self.__trained = False
        self.__classifier = svm.SVC()

    def train(self, input_features, output):
        if len(input_features) != len(output):
            raise Exception("Inconsistent number of input and output training data")

        if len(input_features) == 0:
            raise Exception("Empty training input data list")

        if len(output) == 0:
            raise Exception("Empty training output data list")

        if len(input_features[0]) != self.__features_count:
            raise Exception("Incorrect features count for training data")

        self.__classifier.fit(input_features, output)
        self.__trained = True

    def classify(self, data):
        if not self.__trained:
            raise Exception("Classifier has not been trained yet")

        if len(data) != self.__features_count:
            raise Exception("Incorrect features count for test data")

        return self.__classifier.predict([data])[0]

    def bulk_classify(self, data):
        if not self.__trained:
            raise Exception("Classifier has not been trained yet")

        if len(data[0]) != self.__features_count:
            raise Exception("Incorrect features count for test data")

        return self.__classifier.predict(data)
