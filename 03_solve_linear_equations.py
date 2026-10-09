import numpy as np

# Coefficient matrix
A = np.array([[2, 1],
              [1, 3]])

# Constant vector
B = np.array([5, 6])

# Solve the system AX = B
solution = np.linalg.solve(A, B)

print("Coefficient Matrix:")
print(A)

print("\nConstant Vector:")
print(B)

print("\nSolution:")
print("x =", solution[0])
print("y =", solution[1])

# Verification
print("\nVerification:")
print("Equation 1:", 2 * solution[0] + solution[1])
print("Equation 2:", solution[0] + 3 * solution[1])
