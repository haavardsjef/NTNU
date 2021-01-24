import numpy as np
import matplotlib.pyplot as plt

""" Task 3 """
# Varaibler
omega = 5
a = 2
t_start = 0
t_end = 10

# Funksjonsuttryk


def f(t):
	return np.cos(omega*t) * np.exp(-a*t)


# Plotting
t = np.arange(t_start, t_end, 0.01)
s = f(t)
fig, ax = plt.subplots()
ax.plot(t, s)
plt.show()
