def square_root_method(
    a: list[list[float]], 
    b: list[list[float]]
) -> list[float]: 
    n = len(a)

    y = []
    x = [0] * n

    s = create_S_matrix_from_A(a)
    for i in range(n): 

        summ = 0 
        for k in range(1, i): 
            summ += s[k][i] * y[k]
        
        y.append((b[i] - summ) / s[i][i])

    for i in range(n - 1, -1, -1): 
        summ = 0
        for k in range(i + 1, n): 
            summ += s[i][k] * x[k]

        x[i] = (y[i] - summ) / s[i][i]
    
    return x

def get_transposed_matrix(matrix: list[list[float]]) -> list[list[float]]: 
    n = len(matrix)

    for i in range(n): 
        for j in range(i + 1, n): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
def create_S_matrix_from_A(A: list[list[float]]) -> list[list[float]]: 
    if not check_symmetry(A): 
        print("cannot generate S from non-symmetry matrix A")
        return []
    
    n = len(A)
    S = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n): 
        for j in range(i, n): 
            if j == i: 
                summ = 0 
                for k in range(i): 
                    summ += S[k][i] ** 2

                S[i][i] = (A[i][i] - summ) ** 0.5
            else: 
                summ = 0
                for k in range(i): 
                    summ += S[k][i] * S[k][j]

                S[i][j] = (A[i][j] - summ) / S[i][i]
    
    return S 

def check_symmetry(A: list[list[float]]) -> bool: 
    n = len(A)

    for i in range(n): 
        for j in range(n): 
            if A[i][j] != A[j][i]: 
                return False
        
    return True 