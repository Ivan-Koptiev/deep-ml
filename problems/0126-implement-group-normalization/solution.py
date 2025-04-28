import numpy as np

def group_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, num_groups: int, epsilon: float = 1e-5) -> np.ndarray:
    # Your code here
    B,C,H,W=X.shape
    grouped=X.reshape((B,num_groups,C//num_groups,H,W))

    mean=np.mean(grouped,axis=(2,3,4),keepdims=True)
    var=np.var(grouped,axis=(2,3,4),keepdims=True)

    norm=(grouped-mean)/(np.sqrt(var+epsilon))
    norm_x=norm.reshape((B,C,H,W))

    final=gamma.reshape((1,C,1,1))*norm_x+beta.reshape(1,C,1,1)

    return final