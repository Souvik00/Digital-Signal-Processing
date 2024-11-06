import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
h = np.array([1, 2, 1])
y = np.zeros(len(x) + len(h) - 1)
for n in range(len(y)):
    if n < len(x):
        xx = n
        yy = 0
    else:
        xx = len(x) - 1
        yy = n - len(x) + 1
    while xx >= 0 and yy < len(h):
        y[n] += x[xx] * h[yy]
        xx -= 1
        yy += 1

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
