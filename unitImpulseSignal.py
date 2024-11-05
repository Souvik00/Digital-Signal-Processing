import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(-10, 11)

# Define the unit impulse signal
delta = np.zeros_like(t)
delta[10] = 1

# Sampling frequency
fs = 5

# Sample the signal
delta_sampled = delta[::fs]

# Plot the original and sampled signals
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(t, delta)
plt.title('Unit Impulse Signal')
plt.xlabel('n')
plt.ylabel('δ[n]')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(t[::fs], delta_sampled)
plt.title('Sampled Unit Impulse Signal')
plt.xlabel('n')
plt.ylabel('δ[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
