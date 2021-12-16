from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Initializing wave
wave = np.linspace(0, 1, 1000, endpoint=True)

# Plots a wave of frequncy 97
plt.plot(wave, signal.square(2 * np.pi * 97 * wave))

# Creats title,labels, grid and limits to axes
plt.title('Square wave - frequncy = 97 Hz ')
plt.xlabel('Time in seconds')
plt.ylabel('Amplitude[V]')
plt.grid(True, which='both')
plt.xlim(0, 1.0)
plt.ylim(-2, 2)

# Draws graph
plt.show()
