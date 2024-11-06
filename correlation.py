import numpy as np
import matplotlib.pyplot as plt

# Define the input signals
x = np.array([1, 2, 3, 4, 5])
y = np.array([3,2, 1])

# Lengths of the input signals
n = len(x)
m = len(y)

# Initialize the list to hold cross-correlation values
cross_correlation_full = []

# Calculate cross-correlation for each lag
for lag in range(-m + 1, n):
    sum_product = 0
    for i in range(m):
        j = i + lag
        if 0 <= j < n:
            sum_product += y[i] * x[j]
    cross_correlation_full.append(sum_product)

# Convert the cross-correlation result to a numpy array
cross_correlation_full = np.array(cross_correlation_full)

# Define the lag vector
lags = np.arange(-m + 1, n)

# Plot the input signals
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(np.arange(n), x)
plt.title('Input Signal x')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(np.arange(m), y)
plt.title('Input Signal y')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the cross-correlation result
plt.subplot(3, 1, 3)
plt.stem(lags, cross_correlation_full)
plt.title('Cross-Correlation of x and y')
plt.xlabel('Lag')
plt.ylabel('Cross-Correlation')
plt.grid(True)

plt.tight_layout()
plt.show()
