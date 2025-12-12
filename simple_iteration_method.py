import numpy as np

def simple_iteration_method(A, B, epsilon = 1e-14, iters = 100000): 
    n = len(A)
    
    D = np.zeros((n, n))
    
    for i in range(n): 
        D[i, i] = A[i, i]
    
    E = np.eye(n)
    D_inv = np.linalg.inv(D)
    
    JB = E - D_inv @ A
    G = D_inv @ B
    
    x = np.zeros(n)
    
    for iter in range(iters): 
        x_new = JB @ x + G
        
        if all(abs(x_new - x) < epsilon):
            print(f"{iter=}", f"{epsilon=}")
            return x_new, iter
        
        x = x_new
        
    return x, iter