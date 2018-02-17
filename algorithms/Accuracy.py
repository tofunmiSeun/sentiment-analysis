class Accuracy:

    @staticmethod
    def calculate_precision_and_recall(predicted_values, actual_values):
        if len(predicted_values) != len(actual_values):
            raise Exception

        true_positives = 0
        false_positives = 0
        true_negatives = 0
        false_negatives = 0

        for i in range(0, len(predicted_values)):
            predicted = predicted_values[i]
            actual = actual_values[i]

            if predicted == 1:
                if actual == 1:
                    true_positives += 1
                else:
                    false_positives += 1
            else:
                if actual == 1:
                    false_negatives += 1
                else:
                    true_negatives += 1

        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)

        return {
            "precision": precision,
            "recall": recall
        }

    @staticmethod
    def calculate_f_score(predicted_values, actual_values):
        if len(predicted_values) != len(actual_values):
            raise Exception

        precision_and_recall_values = Accuracy.calculate_precision_and_recall(predicted_values, actual_values)

        precision = precision_and_recall_values["precision"]
        recall = precision_and_recall_values["recall"]

        return (2 * precision * recall) / (precision + recall)
