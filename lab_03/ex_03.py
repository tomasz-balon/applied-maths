import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


def numerical(x, t, r, gamma):
    dxdt = (r*x) - (gamma * (x**2))
    return dxdt


def discrete(x_0, r, K):
    x_prev = x_0

    result = [x_prev]
    x = [0]

    for i in range(1000):
        x_next = x_prev + (r * x_prev * (1 - (x_prev/K) - (x_prev/(r*K))))
        # x_next = x_prev + (r * x_prev * (1 - (x_prev/K)))
        x_prev = x_next
        result.append(x_next)
        x.append(i)

    plt.figure()
    plt.title(f'Discrete solution, r={r}')
    plt.scatter(x, result)


t = np.linspace(0, 100, 10000)
x0 = 100
r_arr = [0.2, 0.8, 2.2, 3.0, 3.4, 3.8, 4.0]
K = 1000

for r in r_arr:
    gamma = (1 + r) / K
    # gamma = r / K
    solution = odeint(numerical, x0, t, args=(r, gamma))

    discrete(x0, r, K)

    plt.figure()
    plt.title(f'Numerical solution, r={r}')
    plt.plot(t, solution[:, 0])

plt.show()
