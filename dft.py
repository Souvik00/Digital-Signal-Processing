import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    X = np.zeros(N, complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Parameters
sampling_rate = 100  # Hz
time_duration = 1  # seconds
num_samples = int(sampling_rate * time_duration)

# Generate a continuous-time signal
t = np.linspace(0, time_duration, 1000)
ct_signal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)

# Sample the continuous-time signal
time_samples = np.linspace(0, time_duration, num_samples)
sampled_signal = np.sin(2 * np.pi * 5 * time_samples) + np.sin(2 * np.pi * 10 * time_samples)

# Calculate the DFT of the sampled signal
dft_signal = dft(sampled_signal)

# Calculate the frequency axis for the DFT
freq_axis = np.fft.fftfreq(num_samples, d=1/sampling_rate)

# Plot the continuous-time signal
plt.figure(figsize=(20, 12))
plt.subplot(6, 1, 1)
plt.plot(t, ct_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Continuous-Time Signal')

# Plot the sampled signal
plt.subplot(6, 1, 2)
plt.stem(time_samples, sampled_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sampled Signal')

# Plot the magnitude spectrum of the DFT
plt.subplot(6, 1, 3)
plt.stem(freq_axis, np.abs(dft_signal))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum of DFT')

# Plot the phase spectrum of the DFT
plt.subplot(6, 1, 4)
plt.stem(freq_axis, np.angle(dft_signal))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.title('Phase Spectrum of DFT')

# Plot the real part of the DFT
plt.subplot(6, 1, 5)
plt.stem(freq_axis, np.real(dft_signal))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Real Part')
plt.title('Real Part of DFT')

# Plot the imaginary part of the DFT
plt.subplot(6, 1, 6)
plt.stem(freq_axis, np.imag(dft_signal))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Imaginary Part')
plt.title('Imaginary Part of DFT')

plt.tight_layout()
plt.show()
