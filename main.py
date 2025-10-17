from gauss_method import gauss_method
from optimal_exclusion_method import optimal_exclusion_method

from utils import print_matrix, print_x
import numpy as np

import copy

matrix = [
    [5, 2, 3, 3],
    [1, 6, 1, 5],
    [3, -4, -2, 8]
]
matrix1 = [
    [2, -1, 5, 10], 
    [1, 1, -3, -2], 
    [2, 4, 1, 1], 
]

matrix_3 = [[1, -1, 4, 3, 1, 6],
    [-1, 4, 6, 2, 1, 7],
    [-1, 2, 3, 2, 3, 8],
    [1, 1, -4, 2, 2, 9],
    [-2, -1, 1, 1, 10, 10]
]

matrix_4 = [[1, -1, 4, 3, 1, 6, 2],
        [-1, 4, 6, 2, 1, 7, -5],
        [-1, 2, 3, 2, 3, 8, 2],
        [1, 1, -4, 2, 2, 9, 7],
        [-2, -1, 1, 1, 10, 10, 15],
        [-6, 7, 3, 0, -4, 2, 6]
        ]


matrixs = [
    matrix,
    matrix1, 
    matrix_3, 
    matrix_4
]

for m in matrixs: 
    A = [s[:-1] for s in m]
    B = [s[-1] for s in m]
    m1 = copy.deepcopy(m)
    print_matrix(m)

    print("ᓚᘏᗢᓚᘏᗢᓚᘏᗢ  метод оптимального исключения  ᓚᘏᗢᓚᘏᗢᓚᘏᗢ")

    X = optimal_exclusion_method(m)
    print_x(X)
    e = np.dot(A, X) - B
    print("максимальная погрешность:")

    print(max(abs(e)))

    print()

    print("ᓚᘏᗢᓚᘏᗢᓚᘏᗢ  метод гаусса  ᓚᘏᗢᓚᘏᗢᓚᘏᗢ")

    X = gauss_method(m1)
    print_x(X)
    e = np.dot(A, X) - B
    print("максимальная погрешность:")
    print(max(abs(e)))

    print()
