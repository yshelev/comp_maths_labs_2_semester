import numpy as np

def check(A, k=10):
    diag_elements = np.diag(A)
    
    max_diag_value = np.max(np.abs(diag_elements))
    
    threshold = np.sqrt(max_diag_value) * 10 ** -k
    
    n = len(A)
    mask = ~np.eye(n, dtype=bool)
    
    off_diag_elements = A[mask]
    
    return np.all(np.abs(off_diag_elements) <= threshold)
    
def rotation_method_with_obstacles(A: np.array, precision=10): 
    n = len(A)
    iters = 1
    cur_p = 1
    while True: 
        C = np.zeros((n, n))
    
        max_value = 0
        ansi = -1
        ansj = -1
        for i, row in enumerate(A): 
            for j, value in enumerate(row): 
                if i != j and abs(value) > max_value: 
                    ansi = i
                    ansj = j
                    max_value = abs(value)
                    
        i = ansi
        j = ansj

        d = np.sqrt((A[i, i] - A[j, j]) ** 2 + 4 * A[i, j] ** 2)
        c = np.sqrt((1 + np.abs(A[i, i] - A[j, j]) / d) / 2)
        sign = 1 if A[i, j] * (A[i, i] - A[j, j]) >= 0 else -1
        s = sign * np.sqrt((1 - np.abs(A[i, i] - A[j, j]) / d) / 2)
        
        C[i, i] = c ** 2 * A[i, i] + 2 * c * s * A[i, j] + s ** 2 * A[j, j]
        C[j, j] = s ** 2 * A[i, i] - 2 * c * s * A[i, j] + c ** 2 * A[j, j]
        C[i, j] = (c**2 - s**2) * A[i, j] + c*s * (A[j, j] - A[i, i])
        C[i, j] = C[j, i]
        
        for k in range(n):
            for l in range(n):
                if k != i and k != j and l != i and l != j:
                    C[k, l] = A[k, l]
                elif k != i and k != j:
                    C[k, i] = c * A[k, i] + s * A[k, j]
                    C[i, k] = C[k, i]

                    C[k, j] = -s * A[k, i] + c * A[k, j]
                    C[j, k] = C[k, j]
        A = C
        if check(A, cur_p):
            cur_p += 1
            if cur_p == precision + 1: 
                print(iters)
                return [A[i, i] for i in range(n)]
        iters += 1
