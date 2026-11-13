# solutions.py — Teacher answers for exercises.py
import numpy as np

# 1
favorite_number = 7
print(favorite_number * 3)

# 2
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# 3
def is_even(n):
    return n % 2 == 0


print("4 is even?", is_even(4))
print("7 is even?", is_even(7))

# 4
M = np.arange(1, 10).reshape(3, 3)
print(M)
print("shape:", M.shape)

# 5
p = np.array([3, 1])
double = np.array([[2, 0],
                   [0, 2]])
print(double @ p)

# 6
rot90 = np.array([[0, -1],
                  [1, 0]])
print(rot90 @ np.array([1, 0]))
