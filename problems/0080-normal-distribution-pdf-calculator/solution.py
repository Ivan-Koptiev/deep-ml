import numpy as np

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
	part1=1/(np.sqrt(2*np.pi*(std_dev)**2))
	part2=np.exp(-((x-mean)**2)/(2*(std_dev)**2))
	val=part1*part2
	return round(val,5)