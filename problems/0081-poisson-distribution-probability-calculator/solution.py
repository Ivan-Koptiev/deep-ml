import math

def poisson_probability(k, lam):
	"""
	Calculate the probability of observing exactly k events in a fixed interval,
	given the mean rate of events lam, using the Poisson distribution formula.
	:param k: Number of events (non-negative integer)
	:param lam: The average rate (mean) of occurrences in a fixed interval
	"""
	# Your code here
	def factorial(x):
		if x==0:
			return 1
		result=1
		for i in range(1,x+1):
			result*=i
		return result

	lam_k=lam**k
	exp_lam=math.exp(-lam)
	fact_k=factorial(k)

	val=(lam_k*exp_lam)/fact_k

	return round(val,5)