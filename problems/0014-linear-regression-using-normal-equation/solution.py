import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round

	theta = np.dot((np.linalg.inv((np.dot(np.transpose(X),X)))),(np.dot(np.transpose(X),y)))
	return theta