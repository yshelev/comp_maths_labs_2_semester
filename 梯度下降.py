import numpy as np

def 梯度下降(A, B, iters = 10000):
    n = len(A)
    x = np.zeros(n)
    for _ in range(iters): 
        r_k = B - A @ x
        
        alpha_k = np.dot(r_k, r_k) / np.dot(A @ r_k, r_k)

        x = x + alpha_k * r_k 
    
    return x