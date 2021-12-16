import matplotlib.pyplot as plt
import numpy as np

# Initialising sine waves
wave1 = np.arange(0, 10, 0.1)
wave2 = np.arange(0, 20, 0.2)
wave3 = np.arange(0, 30, 0.3)
sin_wave1 = np.sin(wave1)
sin_wave2 = np.sin(wave2)
sin_wave3 = np.sin(wave3)
wave2 /= 2

# Creating composite time domain signal
sin_wave4 = sin_wave1+sin_wave2+sin_wave3

# Plotting waves
plt.plot(sin_wave1)
plt.plot(sin_wave2)
plt.plot(sin_wave3)
plt.plot(sin_wave4)

# Setting title, labels, grid and limits to x axis
plt.title('Composite Time Domain Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.xlim(0, 50)
plt.ylim(-2, 3)
plt.grid(True, which='both')

# Draws graph
plt.show()
