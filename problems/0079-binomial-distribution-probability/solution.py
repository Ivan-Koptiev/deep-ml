import math

def binomial_probability(n, k, p):
	"""
    Calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
    each with probability p of success, using the Binomial distribution formula.
    """
	# Your code here

	def factorial(x):
		if x==0:
			return 1
			
		result=1
		for i in range(1,x+1):
			result*=i
		return result

	nk=(factorial(n))/((factorial(k))*(factorial(n-k)))
	q=1-p
	pk=p**k
	qk=q**(n-k)

	probability=nk*pk*qk

	return round(probability, 5)