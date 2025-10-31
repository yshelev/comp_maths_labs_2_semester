from LU_method import LU
import numpy as np
from utils import print_matrix, print_x

a = [
    [5, 1, 0, 9], 
    [4, 2, -1, 4], 
    [8, -1, 4, 1], 
    [5, 7, 4, 6]
]

b = [4, 2, 3, 1]
x = LU(a, b)  

print("максимальная ошибка: ")
print(max(np.dot(a, x) - b))