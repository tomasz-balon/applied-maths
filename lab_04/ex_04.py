import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, RK45
import math


def euler_method(x_prev, h):
    euler_list = []

    for i in range(100000):
        x_next = x_prev + h * equation(x_prev, t[i])
        # x_next = x_prev + (h * math.pi * t[i] * math.cos(x_prev * math.pi * t[i]))
        x_prev = x_next
        euler_list.append(x_next)

    plt.plot(t, euler_list, 'r--', linewidth=6)


def heun_method(x_prev, h):
    heun_list = []

    for i in range(100000):
        # x_next = x_prev + (h * equation(x_prev, t[i])) - (((h ** 2) / math.factorial(2)) * math.pi**2 * t[i]**2 * math.sin(x_prev * math.pi * t[i]))
        # x_next = x_prev + (h/2) * (equation(x_prev, t[i])) + math.pi * t[i] * math.cos(x_prev * math.pi * t[i])
        # x_next = x_prev + h * math.pi * t[i] * math.cos(x_prev * math.pi * t[i]) - (h ** 2) / math.factorial(2) * math.pi**2 * t[i]**2 * math.sin(x_prev * math.pi * t[i])
        k1 = equation(x_prev, t[i])
        k2 = equation((x_prev + h * equation(x_prev, t[i])), (t[i] + h))
        x_next = x_prev + (h/2) * (k1 + k2)
        x_prev = x_next
        heun_list.append(x_next)

    plt.plot(t, heun_list, 'g', linewidth=4)


def runge_kutta_method(x_prev, h):
    runge_kutta_list = []

    for i in range(100000):
        k1 = equation(x_prev, t[i])
        k2 = equation(x_prev + (h/2) * k1, t[i] + (h/2))
        k3 = equation(x_prev + (h/2) * k2, t[i] + (h/2))
        k4 = equation(x_prev + h * k3, t[i] + h)

        x_next = x_prev + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x_prev = x_next
        runge_kutta_list.append(x_next)

    plt.plot(t, runge_kutta_list, 'm', linewidth=2)


def equation(x, t):
    dxdt = math.sin(x*math.pi*t)+math.pi*t*math.cos(math.pi*t)
    return dxdt


t, h = np.linspace(0, 10, 100000, retstep=True)

solution = odeint(equation, 2, t)

plt.plot(t, solution, linewidth=8)

euler_method(2, h)
heun_method(2, h)

plt.show()
