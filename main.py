from square_root_method import square_root_method
from utils import print_matrix, print_x
import numpy as np

A = [
[1, 3, -2, 0, -2], 
[3, 4, -5, 1, -3], 
[-2, -5, 3, -2, 2], 
[0, 1, -2, 5, 3], 
[-2, -3, 2, 3, 4]]

A1 = [
    [2, 1, 4], 
    [1, 1, 3], 
    [4, 3, 14]
]

B1 = [
    16, 12, 52
]

B = [0.5, 5.4, 5.0, 7.5, 3.3]

print_x(x := square_root_method(A, B))

print(max(np.dot(A, x) - B))