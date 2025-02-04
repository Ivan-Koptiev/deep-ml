import numpy as np
def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	# Your code here
	def sig(x):
		return (1/(1+np.exp(-x)))

	return (x*sig(x))