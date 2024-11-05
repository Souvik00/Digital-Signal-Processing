import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])

corr = np.zeros(len(x) + len(y) - 1)
for n in range(len(corr)):
    for k in range(max(0, n - len(y) + 1), min(n + 1, len(x))):
        corr[n] += x[k] * y[n - k]

# Plot the input signal x(n)
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(x)
plt.title('Signal x(n)')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

# Plot the input signal y(n)
plt.subplot(3, 1, 2)
plt.stem(y)
plt.title('Signal y(n)')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)

# Plot the correlation r(n)
plt.subplot(3, 1, 3)
plt.stem(corr)
plt.title('Correlation')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
