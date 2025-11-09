import numpy as np

def border_method(A, B): 
    a_inversed = find_inverse_matrix(A)
    
    return a_inversed @ B.T
    
def find_inverse_matrix(A): 
    n = len(A)
    a_inversed_prev_step = np.array([[1 / A[0][0]]])
        
    for k in range(1, n): 
        u_n = A[:k, k:k + 1]
        v_n = A[k:k + 1, :k]
        a_nn = A[k, k]
              
        beta = a_nn - v_n @ a_inversed_prev_step @ u_n
        alpha_n = 1 / beta
        
        q_n = -alpha_n * (v_n @ a_inversed_prev_step)                 
        r_n = -alpha_n * (a_inversed_prev_step @ u_n) 
        p_n = a_inversed_prev_step + (1 / alpha_n) * (r_n @ q_n) 
        
        temp = np.zeros((k + 1, k + 1))

        temp[:k, :k] = p_n

        temp[:k, k:k + 1] = r_n
        temp[k:k + 1, :k] = q_n
        
        temp[k, k] = alpha_n
        a_inversed_prev_step = temp
        
    
    return a_inversed_prev_step