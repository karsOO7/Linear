import numpy as np

# Create a matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=float)

# Perform SVD
U, S, VT = np.linalg.svd(A)

print("Original Matrix:")
print(A)

print("\nSingular Values:")
print(S)

# Keep only the first singular value
k = 1

U_k = U[:, :k]
S_k = S[:k]
VT_k = VT[:k, :]

# Reconstruct approximate matrix
A_approx = U_k @ np.diag(S_k) @ VT_k

print("\nApproximate Matrix using one component:")
print(np.round(A_approx, 2))
