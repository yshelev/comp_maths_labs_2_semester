import math
import numpy as np
import copy
from utils import print_matrix


def reflection_method(A, B): 
    Q, R = QR_decomposition(A)
    
    n = len(A)
    x = np.zeros(n)
    g = Q.T @ B
    x[n - 1] = g[n - 1] / R[n - 1, n - 1]

    for i in range(n - 2, - 1, - 1):
        summ = sum(R[i, i + 1:n] * x[i + 1:n])
        x[i] = (g[i] - summ) / R[i, i]
    
    return x


def QR_decomposition(A):
    a_clone = copy.deepcopy(A)
    
    
    n = len(a_clone)
    Q = np.eye(n)
    for k in range(n - 1):
        norm_p = np.zeros(n)
        sign = 2 * int(A[k, k] >= 0) - 1
        
        s = sum(a_clone[k:n, k] ** 2)

        norm_p[k] = a_clone[k, k] + sign * np.sqrt(s)

        norm_p[k + 1:n] = a_clone[k + 1:n, k]

        Pk = np.eye(n) - (2 / (np.dot(norm_p, norm_p))) * np.outer(norm_p, norm_p)
        Q = Q @ Pk
        a_clone = Pk @ a_clone

    R = a_clone

    return Q, R