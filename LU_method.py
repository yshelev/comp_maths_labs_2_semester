from utils import print_matrix

def LU(a: list[list[float]], b: list[list[float]]) -> list[float]: 
    l, u = create_LU_from_matrix(a)

    # решаем Ly = B
    

    return l, u

def create_LU_from_matrix(a: list[list[float]]): 
    n = len(a)

    l = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
    u = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n): 
        for j in range(n): 
            if i <= j: 
                u[i][j] = a[i][j] - sum([l[i][k] * u[k][j] for k in range(i)])
            else: 
                l[i][j] = (a[i][j] - sum([l[i][k] * u[k][j] for k in range(j)])) / u[j][j]
    return l, u