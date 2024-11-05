import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(-10, 11)

# Define the unit step signal
u = np.zeros_like(t)
u[10:] = 1

# Sampling frequency
fs = 5

# Sample the signal
u_sampled = u[::fs]

# Plot the original and sampled signals
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(t, u)
plt.title('Unit Step Signal')
plt.xlabel('n')
plt.ylabel('u[n]')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(t[::fs], u_sampled)
plt.title('Sampled Unit Step Signal')
plt.xlabel('n')
plt.ylabel('u[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
