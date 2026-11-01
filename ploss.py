import numpy as np
import matplotlib.pyplot as plt

c = 3e8
f1 = 800e6
f2 = 950e6

d = np.arange(1, 100, 0.1)

pl1 = 20*np.log10(4*np.pi*f1*d/c)
pl2 = 20*np.log10(4*np.pi*f2*d/c)

plt.plot(d, pl1, "b", label="800 MHz")
plt.plot(d, pl2, "r", label="950 MHz")

plt.title("Path Loss Graph")
plt.xlabel("Distance (m)")
plt.ylabel("Path Loss (dB)")
plt.legend()
plt.grid()
plt.show()
