from LU_method import LU
import numpy as np
from utils import print_matrix

a = [
    [5, 1, 0, 9], 
    [4, 2, -1, 4], 
    [8, -1, 4, 1], 
    [5, 7, 4, 6]
]

l, u = LU(a, [4, 2, 3, 1])  
print("l")
print_matrix(l)

print("u")
print_matrix(u)

print("test")

print_matrix(np.dot(l, u))