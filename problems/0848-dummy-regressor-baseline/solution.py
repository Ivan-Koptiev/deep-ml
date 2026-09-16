import numpy as np

def dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None):
    """
    Baseline regressor that predicts a constant value derived from y_train.

    Args:
        y_train: 1D array-like of training target values.
        n_test: number of test predictions to return (int >= 0).
        strategy: one of 'mean', 'median', 'quantile', 'constant'.
        constant: required when strategy='constant'.
        quantile: required when strategy='quantile', must be in [0, 1].

    Returns:
        List[float] of length n_test, all equal to the chosen summary value.
    """
    final=[]
    if strategy == "mean":
        final.extend([np.mean(y_train)] * n_test)
        return final

    elif strategy == "median":
        final.extend([np.median(y_train)] * n_test)
        return final

    elif strategy == "quantile":
        if quantile == None or quantile < 0 or quantile > 1:
            raise ValueError("wrong quantile")
        else:
            final.extend([np.quantile(y_train, quantile)] * n_test)
            return final

    elif strategy == "constant":
        if constant == None:
            raise ValueError("wrong constant")
        else:
            final.extend([constant] * n_test)
            return final
    else:
        raise ValueError("wrong strategy")

