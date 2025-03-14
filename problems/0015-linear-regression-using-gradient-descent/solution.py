import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
	for i in range(iterations):
		hyp=np.dot(X,theta)
		err=hyp-y.reshape(-1,1)
		upd=np.dot(X.T,err)

		theta=theta-(alpha*(1/m)*upd)
	return np.round(theta,4)