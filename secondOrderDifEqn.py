import numpy as np
import matplotlib.pyplot as plt

# Define parameters
a1 = 0.8
a2 = 0.5
N = 100

# Initialize input and output arrays
x = np.zeros(N)
y = np.zeros(N)

# Set initial conditions
y[0] = 1
y[1] = 0.5

# Set input signal (a unit step starting at index 10)
x[10:] = 1

# Iterate through the difference equation
for n in range(2, N):
    y[n] = a1 * y[n-1] + a2 * y[n-2] + x[n]

# Plot the results
plt.stem(range(N), y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Second-Order Difference Equation')
plt.grid(True)
plt.show()
