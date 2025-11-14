def print_matrix(matrix, name=""):
    if name:
        print(f"{name}:")
    for row in matrix:
        print(" ".join(f"{elem:8.3f}" for elem in row))
    print()