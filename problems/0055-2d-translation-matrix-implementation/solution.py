import numpy as np
def translate_object(points, tx, ty):
	trans=[[1,0,tx],[0,1,ty],[0,0,1]]
	for i in range(len(points)):
		points[i].append(1)
	tr=[]
	for i in points:
		pt=np.matmul(trans,i)
		tr.append(pt[:2])
	return tr
