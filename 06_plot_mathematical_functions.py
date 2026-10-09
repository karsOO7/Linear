import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-5, 5, 200)

# Define functions
y1 = x**2
y2 = np.sin(x)

# Plot functions
plt.plot(x, y1, label="y = x^2")
plt.plot(x, y2, label="y = sin(x)")

# Add graph details
plt.xlabel("x")
plt.ylabel("y")
plt.title("Mathematical Functions")
plt.legend()
plt.grid(True)

# Display graph
plt.show()
