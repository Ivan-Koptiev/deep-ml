import numpy as np

def cramers_rule(A, b):
    # Your code here
    x=np.zeros(len(b))
    det_a=np.linalg.det(A)

    if det_a==0:
        return -1
    else:
        for i in range(len(x)):
            new_i=[]
            for j in range(len(A)):
                row=[]
                for k in range(len(A[0])):
                    if k==i:
                        row.append(b[j])
                    else:
                        row.append(A[j][k])
                new_i.append(row)

            det_ai=np.linalg.det(new_i)
            x[i]=det_ai/det_a

    return x