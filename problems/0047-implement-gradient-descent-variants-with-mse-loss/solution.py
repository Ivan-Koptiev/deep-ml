import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
	# Your code here
	def batch(X,y,learning_rate,n_iterations,weights):
		for i in range(n_iterations):
			grad=(2/len(y))*X.T @ (X @ weights - y)
			weights-=learning_rate*grad
		return weights
	
	def stoch(X,y,learning_rate,n_iterations,weights):
		for i in range(n_iterations):
			for j in range(len(y)):
				grad=2*X[j:j+1].T @ (X[j:j+1] @ weights-y[j:j+1])
				weights-=learning_rate*grad
		return weights
	
	def mini(X,y,learning_rate,n_iterations,weights,batch_size):
		for i in range(n_iterations):
			for j in range(0,len(y),batch_size):
				grad=(2/batch_size)*X[j:j+batch_size].T @ (X[j:j+batch_size] @ weights- y[j:j+batch_size])
				weights-=learning_rate*grad
		return weights

	if method=="batch":
		weights=batch(X,y,learning_rate,n_iterations,weights)
	elif method=="stochastic":
		weights=stoch(X,y,learning_rate,n_iterations,weights)
	else:
		weights=mini(X,y,learnin