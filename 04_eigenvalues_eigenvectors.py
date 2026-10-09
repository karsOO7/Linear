import numpy as np

# Define matrix
A = np.array([[4, 1],
              [2, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# Verification for the first eigenvalue/eigenvector
lambda_1 = eigenvalues[0]
v_1 = eigenvectors[:, 0]

print("\nVerification:")
print("A x v =", A @ v_1)
print("lambda x v =", lambda_1 * v_1)
