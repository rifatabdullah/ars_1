# 04_numpy_matrices.py — The same ideas, but with NumPy (much easier!)
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("A =\n", A)
print("shape of A:", A.shape)         # (rows, columns)

print("\nA + B =\n", A + B)
print("\n10 * A =\n", 10 * A)
print("\nA @ B  (matrix multiply) =\n", A @ B)
print("\nA * B  (number-by-number, NOT matrix multiply) =\n", A * B)

# Transpose: rows become columns
print("\nA.T =\n", A.T)

# The identity matrix is the "do nothing" matrix, like multiplying by 1
I = np.eye(2)
print("\nI =\n", I)
print("\nI @ A =\n", I @ A)

# A point / vector is a column of numbers
p = np.array([2, 1])
print("\nA @ p =", A @ p)

# Handy builders
print("\nzeros:\n", np.zeros((2, 3)))
print("\nones:\n", np.ones((3, 2)))
print("\nnumbers 0..8 as a 3x3 grid:\n", np.arange(9).reshape(3, 3))
