import numpy as np

# Define a square matrix
A = np.array([[4, 7],
              [2, 6]])

# Transpose
transpose = A.T

# Determinant
determinant = np.linalg.det(A)

# Inverse
inverse = np.linalg.inv(A)

print("Original Matrix:")
print(A)

print("\nTranspose of Matrix:")
print(transpose)

print("\nDeterminant:")
print(determinant)

print("\nInverse of Matrix:")
print(inverse)
