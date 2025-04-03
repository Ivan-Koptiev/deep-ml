import numpy as np

def cross_product(a, b):
    # Your code here
    c=np.zeros(len(a))
    inds=[0,1,2]
    c[0]=a[1]*b[2]-a[2]*b[1]
    c[1]=a[2]*b[0]-a[0]*b[2]
    c[2]=a[0]*b[1]-a[1]*b[0]

    return c