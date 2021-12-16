from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Initialise wave
t = np.linspace(0, 1, 1000)

# Plots triangle wave of frequency 97
plt.plot(2 * t, signal.sawtooth(2 * np.pi * 97 * t, 0.5))

# Create title, lables, grid and limit to axes
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Triangular wave - frequency = 97 Hz")
plt.grid(True, which='both')
plt.ylim(-2, 2)
plt.xlim(0, 1.0)

# Draws graph
plt.show()
