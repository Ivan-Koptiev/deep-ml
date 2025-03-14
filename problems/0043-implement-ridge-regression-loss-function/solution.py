import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	y_pred=X @ w
	diff=np.power(y_true-y_pred,2)
	err=np.sum(diff)
	bet=np.sum(np.power(w,2))
	loss=(1/len(y_true))*err+alpha*bet
	return np.round(loss,4)
