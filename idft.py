import numpy as np
import matplotlib.pyplot as plt

# Define the frequency-domain signal X[k] (for example, a simple sequence)
X = np.array([1, 2, 3, 4, 5, 4, 3, 2])  # Example frequency-domain signal

# Length of the signal
N = len(X)

# Initialize an array for the time-domain signal x[n]
x = np.zeros(N, dtype=complex)

# Calculate the IDFT manually using the formula
for n in range(N):
    for k in range(N):
        x[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)
    x[n] /= N  # Normalize by N (as per the IDFT formula)

# Plot the real and imaginary parts of the IDFT result
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.stem(range(N), np.real(x), use_line_collection=True)
plt.title('Real part of x[n]')
plt.xlabel('n')
plt.ylabel('Re(x[n])')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(range(N), np.imag(x), use_line_collection=True)
plt.title('Imaginary part of x[n]')
plt.xlabel('n')
plt.ylabel('Im(x[n])')
plt.grid(True)

plt.tight_layout()
plt.show()
