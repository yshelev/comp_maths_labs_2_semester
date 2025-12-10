import numpy as np
from richardson import richardson

A = np.array([
    [4, 1, -2, 0, 1],
    [1, 5, 3, -1, 2],
    [-2, 3, 6, 2, 0],
    [0, -1, 2, 4, -1],
    [1, 2, 0, -1, 3]])
B = np.array([8, 10, 9, 4, 5])

lambdas = richardson(A, B)

print("my lambdas: ")
for lambda_ in sorted(lambdas): 
    print(lambda_)
    
print("np lambdas: ")
numpy_lambdas = np.linalg.eigvals(A)
for lambda_ in sorted(numpy_lambdas): 
    print(lambda_)