import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define variable
x = sp.symbols('x')

# Define function
f = x**2

# Indefinite integration
indefinite_integral = sp.integrate(f, x)

print("Function:")
print(f)

print("\nIndefinite Integral:")
print(indefinite_integral)

# Definite integration from 0 to 3
definite_integral = sp.integrate(f, (x, 0, 3))

print("\nDefinite Integral from 0 to 3:")
print(definite_integral)

# Visualization
x_values = np.linspace(0, 3, 100)
y_values = x_values**2

plt.plot(x_values, y_values, label="y = x^2")
plt.fill_between(x_values, y_values, alpha=0.3)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Integration of y = x^2 from 0 to 3")
plt.legend()
plt.grid(True)
plt.show()
