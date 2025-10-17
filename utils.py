def find_max_value_in_column_and_update(matrix: list[list[float]], c: int) -> None: 
    mv, row = float("-inf"), -1
    for index in range(c, len(matrix)):
        r = matrix[index]
        
        if index < c: 
            continue
        if abs(r[c]) > mv: 
            row = index 
            mv = r[c]
        
        if r[c] == 0: 
            break

    matrix[c], matrix[row] = matrix[row], matrix[c] 

def print_matrix(matrix: list[list[float]]) -> None: 
    n = len(matrix)

    for row in range(n): 
        for column in range(n): 
            print(f"{matrix[row][column]:6.2f}", end=" ")
        print("|", end=" ")
        print(f"{matrix[row][n]:6.2f}")

            
def print_x(X: list[float]) -> None:
    print("вектор X: ")

    for x in X: 
        print(f"{x:.4f}")

    
