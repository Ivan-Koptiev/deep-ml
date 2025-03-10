import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	# Your code here
	def sig(x):
		return (1/(1+np.exp(-x)))

	z=np.dot(X,np.transpose(weights))+bias
	probs=list(map(sig,z))
	preds=[]
	for i in probs:
		if i>=0.5:
			preds.append(1)
		else:
			preds.append(0)
	return preds