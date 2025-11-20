import numpy as np
from simple_iteration_method import simple_iteration_method

A = np.array([
    [4, 1, -2, 0, 1],
    [1, 5, 3, -1, 2],
    [-2, 3, 6, 2, 0],
    [0, -1, 2, 4, -1],
    [1, 2, 0, -1, 3]])
B = np.array([8, 10, 9, 4, 5])

x = simple_iteration_method(A, B)
for x_ in x: 
    print(x_)
    
print(abs(A @ x - B))