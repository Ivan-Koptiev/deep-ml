import numpy as np

def batch_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	# Your code here
	B,C,H,W=X.shape
	means=np.mean(X,axis=(0,2,3),keepdims=True)
	variances=np.var(X,axis=(0,2,3),keepdims=True)
	norm=(X-means)/(np.sqrt(variances+epsilon))
	normalized=norm*gamma.reshape(1,C,1,1)+beta.reshape(1,C,1,1)

					
	return normalized