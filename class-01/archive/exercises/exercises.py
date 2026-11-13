# exercises.py — Class 1 practice! Replace each TODO, then run:
#     python class-01/exercises/exercises.py
import numpy as np

# ---------------------------------------------------------------------
# 1. Python warm-up
# Make a variable `favorite_number` and print it multiplied by 3.
# TODO


# ---------------------------------------------------------------------
# 2. Loop practice
# Print the 5 times table from 5 x 1 up to 5 x 10.
# TODO


# ---------------------------------------------------------------------
# 3. Write a function `is_even(n)` that returns True if n is even.
def is_even(n):
    # TODO
    pass


print("4 is even?", is_even(4))   # should be True
print("7 is even?", is_even(7))   # should be False

# ---------------------------------------------------------------------
# 4. Matrix basics
# Create a 3x3 NumPy matrix M with the numbers 1..9 and print its shape.
# TODO


# ---------------------------------------------------------------------
# 5. Transform a point
# The point p = (3, 1). Build a matrix that DOUBLES its size, apply it with @,
# and print the result. Expected: [6 2]
p = np.array([3, 1])
# TODO


# ---------------------------------------------------------------------
# 6. Challenge 🌟
# Find the 2x2 matrix that rotates by 90° counter-clockwise.
# Apply it to (1, 0). You should get (0, 1).
# Hint: rotation = [[cos θ, -sin θ], [sin θ, cos θ]]
# TODO
