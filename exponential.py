import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(-10, 11)

# Define the exponential signal
a = 0.8  # Decay factor
x = a**t

# Sampling frequency
fs = 5

# Sample the signal
x_sampled = x[::fs]

# Plot the original and sampled signals
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(t, x)
plt.title('Exponential Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(t[::fs], x_sampled)
plt.title('Sampled Exponential Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
