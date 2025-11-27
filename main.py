import numpy as np
from 梯度下降 import 梯度下降

A = np.array([
    [4, 1, -2, 0, 1],
    [1, 5, 3, -1, 2],
    [-2, 3, 6, 2, 0],
    [0, -1, 2, 4, -1],
    [1, 2, 0, -1, 3]])
B = np.array([8, 10, 9, 4, 5])

x = 梯度下降(A, B)

print("найденный вектор X: ")
for x_ in x: 
    print(x_)
print()

print("Максимальная ошибка выражения A @ x - B")  
print(max(abs(A @ x - B)))