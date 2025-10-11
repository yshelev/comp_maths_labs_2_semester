def gauss_method(matrix: list[list[float]]) -> list[float]:
    for c in range(0, len(matrix)): 
        find_max_value_in_column_and_update(matrix, c)
        if matrix[c][c] == 0: 
            continue
        for i in range(c + 1, len(matrix)): 
            if matrix[i][c] == 0: 
                continue
            k = matrix[c][c] / matrix[i][c]

            for j in range(c, len(matrix) + 1): 
                matrix[i][j] = matrix[c][j] - matrix[i][j] * k
    return recover_answer_by_matrix(matrix)

def recover_answer_by_matrix(matrix: list[list[float]]) -> list[float]:
    x_list: list[float] = []
    for r in range(len(matrix) - 1, -1, -1): 
        x_list.append(
            solution_of_linear_equation(
                matrix[r][r],
                matrix[r][-1] - sum([x * matrix[r][len(matrix) - index - 1] for index, x in enumerate(x_list)])
            )
        )
    
    return x_list[::-1]

def solution_of_linear_equation(a: float, b: float): 
    return b / a 


def find_max_value_in_column_and_update(matrix: list[list[float]], c: int) -> bool: 
    mv, row = float("-inf"), -1
    for index, r in enumerate(matrix):
        if index < c: 
            continue
        if abs(r[c]) > mv: 
            row = index 
            mv = r[c]
        
        if r[c] == 0: 
            break

    matrix[c], matrix[row] = matrix[row], matrix[c] 