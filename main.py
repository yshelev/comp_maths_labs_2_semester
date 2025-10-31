from square_root_method import square_root_method
from utils import print_matrix, print_x
import numpy as np

A = [
    [2.2, 4, -3, 1.5, 0.6, 2, 0.7], 
    [4, 3.2, 1.5, -0.7, -0.8, 3, 1], 
    [-3, 1.5, 1.8, 0.9, 3, 2, 2], 
    [1.5, -0.7, 0.9, 2.2, 4, 3, 1], 
    [0.6, -0.8, 3, 4, 3.2, 0.6, 0.7], 
    [2, 3, 2, 3, 0.6, 2.2, 4], 
    [0.7, 1, 2, 1, 0.7, 4, 3.2]
]

A1 = [
    [2, 1, 4], 
    [1, 1, 3], 
    [4, 3, 14]
]

B1 = [
    16, 12, 52
]

B = [3.2, 4.3,  -0.1, 3.5, 5.3, 9, 3.7]

x = square_root_method(A, B)
print(max(np.dot(A, x) - B))