import numpy as np

def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
	
	def tf_calc(t,d):
		n_t=0
		for i in corpus[d]:
			if i==t:
				n_t+=1
		return n_t/len(corpus[d])

	def idf_calc(t):
		n=len(corpus)
		df=0
		for i in corpus:
			if t in i:
				df+=1
		return np.log((n+1)/(df+1))+1

	tf=[]
	idf=[]
	
	for i in range(len(query)):
		idf.append(idf_calc(query[i]))
		row=[]
		for j in range(len(corpus)):
			row.append(tf_calc(query[i],j))
		tf.append(row)

	idf=np.array(idf).reshape(-1,1)
	tf=np.array(tf)
	tf_idf=tf*idf
	tf_idf=np.transpose(tf_idf)
	return np.round(tf_idf,5)
