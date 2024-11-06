import numpy as np
import matplotlib.pyplot as plt

# Define the transfer function
def transfer_function(freq, a):
    z = np.exp(-1j * freq)
    return 1 / (1 - a * z)

# Parameters
a = 0.9  # Filter coefficient
fs = 1000  # Sampling frequency
f_range = np.linspace(0, fs/2, 1000)  # Frequency range

# Calculate the frequency response
freq_response = transfer_function(2 * np.pi * f_range / fs, a)

# Extract the phase response
phase_response = np.angle(freq_response)

# Plot the phase response
plt.figure()
plt.plot(f_range, phase_response)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.title('Phase Response of a Low-Pass Filter')
plt.grid(True)
plt.show()
