import numpy as np

def relaxation_method(A, B, omega, max_iter=100000, epsilon=1e-14): 
    n = len(A)
    x = np.zeros(n)
    for iters in range(max_iter):
        x_new = np.zeros(n)
        
        for i in range(n):
            sum_l = sum(A[i][j] * x_new[j] for j in range(i))
            sum_v = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (B[i] - sum_l - sum_v)

        if np.all(np.abs(x - x_new) < epsilon):
            x = x_new
            break

        x = x_new
    
    return x, iters

        
        
        