import numpy as np
import matplotlib.pyplot as plt

# Define parameters
a = 0.8  # Coefficient
N = 100  # Number of samples

# Initialize input and output arrays
x = np.zeros(N)
y = np.zeros(N)

# Set initial condition and input signal
y[0] = 1
x[10:] = 1

# Iterate through the difference equation
for n in range(1, N):
    y[n] = a * y[n-1] + x[n]

# Plot the results
plt.stem(range(N), y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('First-Order Difference Equation')
plt.grid(True)
plt.show()
