import numpy as np
import matplotlib.pyplot as plt

# Define function and derivative
def function(x):
    return x**2

def derivative(x):
    return 2 * x

# Initial value
x = 5.0

# Learning rate
learning_rate = 0.1

# Number of iterations
iterations = 20

x_values = []
y_values = []

# Gradient Descent
for i in range(iterations):
    x_values.append(x)
    y_values.append(function(x))

    gradient = derivative(x)
    x = x - learning_rate * gradient

print("Final value of x:", x)
print("Final function value:", function(x))

# Visualization
plt.plot(x_values, y_values, marker='o')
plt.xlabel("Iteration")
plt.ylabel("Function Value")
plt.title("Gradient Descent Optimization")
plt.grid(True)
plt.show()
