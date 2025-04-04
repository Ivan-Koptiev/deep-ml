import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
    num_vars = len(b)
    if x_ini is None:
        x = np.zeros(num_vars)
    else:
        x = x_ini.copy()

    for _ in range(n):
        x_new = x.copy()
        for i in range(num_vars):
            
            s1 = np.dot(A[i, :i], x_new[:i])
            
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        x = x_new
		
    return x