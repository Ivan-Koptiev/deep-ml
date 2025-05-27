import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    # Your code here
    predicted=np.clip(predicted_probs, epsilon, 1-epsilon)
    L=(-1/predicted_probs.shape[0])*np.sum(np.sum(true_labels*np.log(predicted),axis=1), axis=0)+epsilon

    return L