def print_matrix(matrix: list[list[float]]) -> None: 
    n = len(matrix)
    flag = True 

    if len(matrix) == len(matrix[0]): 
        flag = False

    for row in range(n): 
        for column in range(n): 
            print(f"{matrix[row][column]:6.2f}", end=" ")
        if flag: 
            print("|", end=" ")
            print(f"{matrix[row][n]:6.2f}")
        else: 
            print()

            
def print_x(X: list[float]) -> None:
    for x in X: 
        print(f"{x:.4f}")