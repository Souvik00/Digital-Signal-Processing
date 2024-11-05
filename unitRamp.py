import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.arange(-10, 11)

# Define the unit ramp signal
r = t * (t >= 0)

# Sampling frequency
fs = 5

# Sample the signal
r_sampled = r[::fs]

# Plot the original and sampled signals
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(t, r)
plt.title('Unit Ramp Signal')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(t[::fs], r_sampled)
plt.title('Sampled Unit Ramp Signal')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
