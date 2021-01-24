import numpy as np
from matplotlib import pyplot as plt

# Konstanter
c1 = 3
c2 = 0.8
t_start = 0.0
t_end = 2.0


def v(t):
	return (c1/2)*(t**2)-(c2/4)*(t**4)


# Plotting
t = np.arange(t_start, t_end, 0.01)
s = v(t)
fig, ax = plt.subplots()
ax.plot(t, s)
plt.show()


# Finn arealet numerisk
def simpsons(f, a, b, N=20):
    delta_x = (b-a)/N
    x = np.linspace(a, b, N+1)
    y = f(x)
    S = delta_x/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


print(simpsons(v, 0, 2))
