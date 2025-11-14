import numpy as np
from utils import print_matrix

def border_method(A, B): 
    a_inversed = find_inverse_matrix(A)
    print("Обратная матрица для матрицы А:")
    print_matrix(a_inversed)

    print("Проверка (A * A-1 = E)")
    print_matrix(a_inversed @ A)
    return a_inversed @ B.T
    
def find_inverse_matrix(A): 
    n = len(A)
    a_inversed_prev_step = np.array([[1 / A[0][0]]])
    
    print("матрица обратная к A на 1-ом шаге")
    print_matrix(a_inversed_prev_step)
        
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
        print(f"матрица обратная к A на {k + 1}-ом шаге")
        print_matrix(a_inversed_prev_step)
        
    
    return a_inversed_prev_step