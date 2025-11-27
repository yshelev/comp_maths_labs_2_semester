import numpy as np

def 梯度下降(A, B, iters = 10000, epsilon=1e-16):
    n = len(A)
    x = np.zeros(n)
    for iter in range(iters): 
        r_k = B - A @ x
        
        alpha_k = np.dot(r_k, r_k) / np.dot(A @ r_k, r_k)

        x_new = x + alpha_k * r_k 
        if all(abs(x_new - x) < epsilon): 
            print(f"{iter=}", f"{epsilon=}")
        x = x_new
    
    return x