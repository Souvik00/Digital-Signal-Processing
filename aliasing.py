import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.linspace(0, 1, 1000)

# Define the original signals
x1 = np.sin(2 * np.pi * 10 * t)
x2 = np.sin(2 * np.pi * 50 * t)

# Sampling frequency
fs = 40

# Sample the signals
x1_sampled = x1[::int(len(x1) / fs)]
x2_sampled = x2[::int(len(x2) / fs)]

# Plot the original and under-sampled signals
plt.figure(figsize=(20, 12))

plt.subplot(4, 1, 1)
plt.plot(t, x1)
plt.title('Original Signal 1 (10 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(4, 1, 2)
plt.stem(t[::int(len(t) / fs)], x1_sampled)
plt.title('Under-sampled Signal 1 (10 Hz)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, x2)
plt.title('Original Signal 2 (50 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(4, 1, 4)
plt.stem(t[::int(len(t) / fs)], x2_sampled)
plt.title('Under-sampled Signal 2 (50 Hz)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
