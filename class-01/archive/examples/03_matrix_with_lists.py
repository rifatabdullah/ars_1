# 03_matrix_with_lists.py — Building matrices by hand with plain Python lists

# A matrix is a grid of numbers: a list of rows
A = [
    [1, 2],
    [3, 4],
]
B = [
    [5, 6],
    [7, 8],
]

print("A has", len(A), "rows and", len(A[0]), "columns")
print("Row 0 of A:", A[0])
print("A[1][0] (row 1, column 0):", A[1][0])   # -> 3


def show(matrix, title):
    print(title)
    for row in matrix:
        print("  ", row)


def add(M, N):
    """Add two matrices of the same size, number by number."""
    rows, cols = len(M), len(M[0])
    return [[M[r][c] + N[r][c] for c in range(cols)] for r in range(rows)]


def scale(k, M):
    """Multiply every number in M by k."""
    return [[k * x for x in row] for row in M]


def multiply(M, N):
    """Matrix multiplication: row of M  •  column of N."""
    result = []
    for r in range(len(M)):
        new_row = []
        for c in range(len(N[0])):
            total = 0
            for k in range(len(N)):
                total += M[r][k] * N[k][c]
            new_row.append(total)
        result.append(new_row)
    return result


show(A, "A =")
show(B, "B =")
show(add(A, B), "A + B =")
show(scale(10, A), "10 × A =")
show(multiply(A, B), "A × B =")
show(multiply(B, A), "B × A =  (different! order matters)")
