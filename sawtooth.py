import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Initializing wave
timePoints = np.linspace(0, 1, 1000)

# Plots a sawtooth wave of frequency 97
plt.plot(timePoints, signal.sawtooth(2 * np.pi * 97 * timePoints))

# Setting title, labels, grid and limit to axis
plt.title('Sawtooth wave - 97  Hz')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.ylim(-2, 2)
plt.xlim(0, 1.0)

# Draws graph
plt.show()
