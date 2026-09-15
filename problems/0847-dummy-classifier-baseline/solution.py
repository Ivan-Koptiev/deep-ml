import numpy as np

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    predictions = []

    if strategy == "most_frequent":
        label = max(y_train, key=y_train.count)
        for i in range(n_test):
            predictions.append(label)

    elif strategy == "constant":
        for i in range(n_test):
            predictions.append(constant)

    elif strategy == "uniform":
        sorted_classes = sorted(set(y_train))
        n_classes = len(sorted_classes)

        for i in range(n_test):
            predictions.append(sorted_classes[i % n_classes])

    else:  # stratified
        sorted_classes = sorted(set(y_train))

        class_freq = []
        for i in range(len(sorted_classes)):
            f_c = y_train.count(sorted_classes[i]) / len(y_train)
            class_freq.append(f_c)

        # Exact desired number of predictions for each class
        exact_counts = np.array(class_freq) * n_test

        # Start by flooring all counts
        n_items = np.floor(exact_counts).astype(int)

        # How much was lost by flooring each class
        fractional_parts = exact_counts - n_items

        # Number of predictions we still need
        remainder = n_test - sum(n_items)

        # Sort indices by:
        #   1. largest fractional part
        #   2. smaller class first in a tie
        indices = sorted(
            range(len(sorted_classes)),
            key=lambda i: (-fractional_parts[i], sorted_classes[i])
        )

        # Give ONE extra prediction to each of the top classes
        for i in indices[:remainder]:
            n_items[i] += 1

        # Build predictions in sorted class order
        for i in range(len(n_items)):
            predictions.extend([sorted_classes[i]] * n_items[i])

    return predictions