import numpy as np

def richardson(A: np.array, B: np.array, epsilon=1e-10):
    n = len(A)
    x_new = np.zeros(n)
    
    eigenvalue_max = max(np.linalg.eigvals(A))
    eigenvalue_min = min(np.linalg.eigvals(A))
    theta = eigenvalue_min / eigenvalue_max
    rho_0 = (1 - theta) / (1 + theta)
    tau_0 = 2 / (eigenvalue_max + eigenvalue_min)
    v_k = np.cos(((-1) * np.pi) / max_iter)
    x_new = B * tau_0 / (1 + rho_0 * v_k) * np.ones(n)
    rho_1 = (1 - np.sqrt(theta)) / (1 + np.sqrt(theta))
    max_iter = np.log(2 / epsilon) / np.log(1 / rho_1)
    for k in range(1, max_iter):
        v_k = np.cos(((2 * k - 1) * np.pi) / max_iter)
        x_new = B * tau_0 / (1 + rho_0 * v_k) * x_new
       
    return x_new 
        

     