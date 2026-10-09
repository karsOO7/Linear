import sympy as sp

# Define variables
x, y = sp.symbols('x y')

# Single-variable function
f = x**3 + 2*x**2 + x

# Calculate derivative
derivative = sp.diff(f, x)

print("Function:")
print(f)

print("\nDerivative:")
print(derivative)

# Multivariable function
g = x**2 + y**2 + 3*x*y

# Partial derivatives
gx = sp.diff(g, x)
gy = sp.diff(g, y)

print("\nMultivariable Function:")
print(g)

print("\nPartial derivative with respect to x:")
print(gx)

print("\nPartial derivative with respect to y:")
print(gy)

print("\nGradient:")
print([gx, gy])
