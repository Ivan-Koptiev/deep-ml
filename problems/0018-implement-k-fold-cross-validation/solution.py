import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    # Your code here
    indicies=np.arange(len(X))

    if shuffle:
        if random_seed is not None:
            np.random.seed(random_seed)
        np.random.shuffle(indicies)

    fold_size=len(X) // k
    folds=[indicies[i*fold_size:(i+1)*fold_size] for i in range(k)]

    remainder=len(X) % k
    for i in range(remainder):
        folds[i]=np.append(folds[i],indicies[k*fold_size+i])

    train_test_splits=[]
    for i in range(k):
        test_indicies=folds[i]
        train_indicies=np.concatenate([folds[j] for j in range(k) if j!=i])
        train_test_splits.append((train_indicies.tolist(), test_indicies.tolist()))

    return train_test_splits