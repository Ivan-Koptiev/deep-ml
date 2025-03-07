import numpy as np

def layer_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	"""
	Perform Layer Normalization.
	"""
	# Your code here
	mean=np.mean(X, axis=-1)
	var=np.var(X,axis=-1)
	mean=mean.reshape(mean.shape[0],mean.shape[1],1)
	var=var.reshape(var.shape[0],var.shape[1],1)
	norm=(X-mean)/(np.sqrt(var+epsilon))
	gamma=gamma.reshape((X.shape[2],))
	beta=beta.reshape((X.shape[2],))
	final=gamma*norm+beta

	return final