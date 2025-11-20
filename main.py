import numpy as np
from simple_iteration_method import simple_iteration_method
from relaxation_method import relaxation_method

A = np.array([
    [4, 1, -2, 0, 1],
    [1, 5, 3, -1, 2],
    [-2, 3, 6, 2, 0],
    [0, -1, 2, 4, -1],
    [1, 2, 0, -1, 3]])
B = np.array([8, 10, 9, 4, 5])

omega = 1

x = simple_iteration_method(A, B)
for x_ in x: 
    print(x_)
    
print(abs(A @ x - B))


x = relaxation_method(A, B, omega)

for x_ in x: 
    print(x_)
    
print(abs(A @ x - B))