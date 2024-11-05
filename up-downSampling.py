import numpy as np
import matplotlib.pyplot as plt

# Original signal
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# UP-sampling factor
L = 3

# Up-sampled signal
x_up = np.zeros(len(x) * L)
x_up[::L] = x

# Down-sampling factor
M = 2

# Down-sampled signal
x_down = x[::M]

# Plot the original and down-sampled signals
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(x)
plt.title('Original Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(x_up)
plt.title('Up-sampled Signal (L = {})'.format(L))
plt.xlabel('n')
plt.ylabel('x_up[n]')
plt.grid(True)


plt.subplot(3, 1, 3)
plt.stem(x_down)
plt.title('Down-sampled Signal (M = {})'.format(M))
plt.xlabel('n')
plt.ylabel('x_down[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
