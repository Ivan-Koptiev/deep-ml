def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	props=[]
	tot=len(apples)
	sum=0
	for i in set(apples):
		count=0
		for j in apples:
			if j==i:
				count+=1
		props.append(count/tot)
	for i in props:
		sum+=i**2
	g=1-sum
	return g