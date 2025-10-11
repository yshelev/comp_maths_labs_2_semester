def optimal_exclusion_method(matrix: list[list[float]]) -> list[float]:
    n = len(matrix)

    for k in range(n): 
        for i in range(0, k): 
            coefficient = matrix[k][i]

            for j in range(0, n + 1): 
                matrix[k][j] = matrix[i][j] * coefficient - matrix[k][j]

        leading_element = matrix[k][k]
        for j in range(k, n + 1): 
            matrix[k][j] /= leading_element

        for j in range(0, k):
            coefficient = matrix[j][k]

            for i in range(k, n + 1): 
                matrix[j][i] -= matrix[k][i] * coefficient
            
    return [matrix[i][-1] for i in range(n)]