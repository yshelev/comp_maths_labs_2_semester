from gauss_method import gauss_method
from optimal_exclusion_method import optimal_exclusion_method

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

    matrixs = [
        matrix,
        matrix1
    ]

    for m in matrixs: 
        print("matrix", m)
        print("optimal exclusion method")
        print(optimal_exclusion_method(m))
        print("gauss method")
        print(gauss_method(m))

    print()

if __name__ == "__main__": 
    main()