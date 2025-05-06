import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
v = 5  # 速度[m/s]
x = v * t  # 位置[m]

plt.plot(t, x)
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')
plt.title('Uniform Linear Motion')
plt.grid(True)
plt.show()
