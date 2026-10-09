import numpy as np

# Define two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix Addition
addition = A + B

# Matrix Multiplication
multiplication = A @ B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition (A + B):")
print(addition)

print("\nMatrix Multiplication (A x B):")
print(multiplication)
