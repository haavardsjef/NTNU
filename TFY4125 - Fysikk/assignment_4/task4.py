# Task 4b

import matplotlib.pyplot as plt
import numpy as np

l = 10
g = 9.81
m1 = 1.0


def v2e(m2):
    return ((2*g*l)**(0.5))*((2*m1)/(m1+m2))


m2 = np.arange(0.0, 2.0, 0.01)
v2 = v2e(m2)
plt.plot(m2, v2)

plt.xlabel('m2 (kg)')
plt.ylabel('V2e (m/s)')
plt.title('Hastighet vs m2, (m1 = 1.0kg, l=10m)')
plt.grid(True)
plt.savefig("test.png")
plt.show()
