import numpy as np

def relaxation_method(A, B, omega, iters=10000, epsilon=1e-16): 
    n = len(A)
    x = np.zeros(n)
    
    for iter in range(iters): 
        x_prev = x.copy() 
        for i in range(n): 
            x[i] = (1 - omega) * x_prev[i] + (omega / A[i, i]) * (B[i] -
                                                                  np.dot(A[i, :i], x[:i]) - 
                                                                  np.dot(A[i, i+1:], x_prev[i+1:]) )
        if all(abs(x - x_prev) < epsilon):
            return x, iters
        
    return x

        
        
        