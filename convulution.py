import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
h = np.array([1, 2, 1])
y = np.zeros(len(x) + len(h) - 1)
for n in range(len(y)):
    for k in range(max(0, n - len(h) + 1), min(n + 1, len(x))):
        y[n] += x[k] * h[n - k]

# Plot the input signal
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(x)
plt.title('Input Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

# Plot the impulse response
plt.subplot(3, 1, 2)
plt.stem(h)
plt.title('Impulse Response')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)

# Plot the output signal
plt.subplot(3, 1, 3)
plt.stem(y)
plt.title('Output Signal (Convolution)')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
