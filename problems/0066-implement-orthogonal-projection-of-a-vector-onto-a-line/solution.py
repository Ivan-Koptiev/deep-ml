
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	proj=[]
	v_l=[]
	l_l=[]
	vl_ll=[]
	for i in range(len(v)):
		v_l.append(v[i]*L[i])
	for i in L:
		l_l.append(i*i)
	for i in range(len(v_l)):
		if l_l[i]!=0:
			vl_ll.append(v_l[i]/l_l[i])
		else:
			vl_ll.append(0.0)
	for i in range(len(vl_ll)):
		proj.append(vl_ll[i]*L[i])


	return proj
