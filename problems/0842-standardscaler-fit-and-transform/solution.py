import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    #scaler
    mean_columns=np.mean(X_train, axis=0)
    std_columns=np.std(X_train, axis=0)
    for i in range(len(std_columns)):
        if std_columns[i] == 0:
            std_columns[i] = 1.0
    scaled_x_test=(X_test-mean_columns)/std_columns

    return scaled_x_test
