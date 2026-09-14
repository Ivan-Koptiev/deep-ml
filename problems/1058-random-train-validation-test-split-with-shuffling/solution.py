import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n=data.shape[0]
    new_data=data[np.random.default_rng(seed).permutation(n)]
    train_end=int(n*train_frac)
    validation_end=train_end+int(n*validation_frac)
    train=new_data[0:train_end]
    validation=new_data[train_end:validation_end]
    test=new_data[validation_end:]
    final=[train, validation, test]
    return final