from LU_method import LU
import numpy as np
from utils import print_matrix, print_x

a = [
    [5, 1, 0, 9], 
    [4, 2, -1, 4], 
    [8, -1, 4, 1], 
    [5, 7, 4, 6]
]

x = LU(a, [4, 2, 3, 1])  
print_x(x)