from border_method import find_inverse_matrix
import numpy as np

A = np.array([
    [4, 1, 2], 
    [5, 2, 1], 
    [9, 2, 3]
]) 

print(find_inverse_matrix(A))