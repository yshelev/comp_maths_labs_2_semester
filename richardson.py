import numpy as np

def richardson(A: np.array, B: np.array, epsilon=1e-14):
    n = len(A)
    x_new = np.zeros(n)
    
    eigenvalue_max = max(np.linalg.eigvals(A))
    eigenvalue_min = min(np.linalg.eigvals(A))
    theta = eigenvalue_min / eigenvalue_max
    rho_0 = (1 - theta) / (1 + theta)
    tau_0 = 2 / (eigenvalue_max + eigenvalue_min)
    v_k = np.cos(((-1) * np.pi) / (2 * n))
    tau_k = tau_0 / (1 + rho_0 * v_k)
    x_new = B * tau_k / (1 + rho_0 * v_k) * np.ones(n)
    rho_1 = (1 - np.sqrt(theta)) / (1 + np.sqrt(theta))
    max_iter = int(np.log(2 / epsilon) / np.log(1 / rho_1)) + 2
    for k in range(1, max_iter + 10000):
        v_k = np.cos(((2 * k - 1) * np.pi) / (2 * n))
        tau_k = tau_0 / (1 + rho_0 * v_k)
        r = B - A @ x_new
        x_new = x_new + tau_k * r
       
    return x_new 
        

     