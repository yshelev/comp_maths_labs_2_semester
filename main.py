from gauss_method import gauss_method
from optimal_exclusion_method import optimal_exclusion_method

import numpy as np

def main(): 
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

        X = optimal_exclusion_method(m)
        e = np.dot(A, X) - B

        print(e)

        print()



    print()

if __name__ == "__main__": 
    main()