# Task 4b

import matplotlib.pyplot as plt
import numpy as np


def func(theta):
    return 0.5*(1+np.cos(theta))


m2 = np.arange(0.0, 2*np.pi, 0.01)
v2 = func(m2)
plt.plot(m2, v2)

plt.xlabel('Radianer')
plt.ylabel('Kf/Ki')
plt.grid(True)
plt.savefig("test.png")
plt.show()
