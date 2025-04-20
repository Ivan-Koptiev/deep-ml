import numpy as np

def noisy_topk_gating(
    X: np.ndarray,
    W_g: np.ndarray,
    W_noise: np.ndarray,
    N: np.ndarray,
    k: int
) -> np.ndarray:
    """
    Args:
        X: Input data, shape (batch_size, features)
        W_g: Gating weight matrix, shape (features, num_experts)
        W_noise: Noise weight matrix, shape (features, num_experts)
        N: Noise samples, shape (batch_size, num_experts)
        k: Number of experts to keep per example
    Returns:
        Gating probabilities, shape (batch_size, num_experts)
    """
    h_b = X @ W_g
    h_n = X @ W_noise

    softp_h_n = np.log(1 + np.exp(h_n)) 

    H = h_b + (N * softp_h_n)

    def soft(x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True)) 
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    
    def topK(x, k):
        sort_inds = np.argsort(x, axis=1)[:, -k:]
        mask = np.zeros_like(x, dtype=bool) 
        for i, inds in enumerate(sort_inds):