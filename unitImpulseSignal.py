import numpy as np
import matplotlib.pyplot as plt

# Define the continuous time vector
t_cont = np.linspace(-1, 1, 1000)  # From -1 to 1 with 1000 points

# Define the unit impulse signal in continuous time
delta_cont = np.zeros_like(t_cont)
delta_cont[np.abs(t_cont) < 0.01] = 1  # Impulse at t = 0, approximated by a small interval

# Define the discrete time vector
t_disc = np.arange(-10, 11)

# Define the unit impulse signal in discrete time
delta_disc = np.zeros_like(t_disc)
delta_disc[10] = 1  # Impulse at n = 0 (index 10 in the array)

# Sampling frequency
fs = 5

# Sample the discrete-time signal
delta_sampled = delta_disc[::fs]

# Plot the continuous-time unit impulse signal
plt.figure(figsize=(20, 8))

plt.subplot(2, 2, 1)
plt.plot(t_cont, delta_cont)
plt.title('Continuous-Time Unit Impulse Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the discrete-time unit impulse signal
plt.subplot(2, 2, 2)
plt.stem(t_disc, delta_disc)
plt.title('Discrete-Time Unit Impulse Signal')
plt.xlabel('n')
plt.ylabel('δ[n]')
plt.grid(True)

# Plot the sampled discrete-time unit impulse signal
plt.subplot(2, 2, 3)
plt.stem(t_disc[::fs], delta_sampled)
plt.title('Sampled Discrete-Time Unit Impulse Signal')
plt.xlabel('n')
plt.ylabel('δ[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
