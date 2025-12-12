import numpy as np
from rotation_method_with_obstacles import rotation_method_with_obstacles

A = np.array([
    [4, 1, -2, 0, 1],
    [1, 5, 3, -1, 2],
    [-2, 3, 6, 2, 0],
    [0, -1, 2, 4, -1],
    [1, 2, 0, -1, 3]])
A = np.array([
    [1, 2], 
    [2, 1]    
])
lambdas = rotation_method_with_obstacles(A)

print("my lambdas: ")
for lambda_ in sorted(lambdas): 
    print(lambda_)
    
print("np lambdas: ")
numpy_lambdas = np.linalg.eigvals(A)
for lambda_ in sorted(numpy_lambdas): 
    print(lambda_)
    
print(max(abs(l1 - l2) for l1, l2 in zip(lambdas, numpy_lambdas)))