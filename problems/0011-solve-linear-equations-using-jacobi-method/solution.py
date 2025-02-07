import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    
    x = np.zeros(len(b))
    x_new = np.copy(x) 

    for _ in range(n): 
        for i in range(len(A)):
            sum = 0
            for j in range(len(A)):
                if i != j:
                    sum += A[i][j] * x[j]  
            x_new[i] = (b[i] - sum) / A[i][i] 

        
        x = np.copy(x_new)

    return x