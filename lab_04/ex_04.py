import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math


def euler_method(x_prev, h, max_value):
    euler_list = []

    for i in range(max_value):
        x_next = x_prev + h * equation(x_prev, t[i])
        x_prev = x_next
        euler_list.append(x_next)

    plt.plot(t, euler_list, 'r--', linewidth=1.5, label='Euler approximation')
    return euler_list


def heun_method(x_prev, h, max_value):
    heun_list = []

    for i in range(max_value):
        k1 = equation(x_prev, t[i])
        k2 = equation((x_prev + h * equation(x_prev, t[i])), (t[i] + h))
        x_next = x_prev + (h/2) * (k1 + k2)
        x_prev = x_next
        heun_list.append(x_next)

    plt.plot(t, heun_list, 'g--', linewidth=1.5, label='Heun approximation')
    return heun_list


def runge_kutta_method(x_prev, h, max_value):
    runge_kutta_list = []

    for i in range(max_value):
        k1 = equation(x_prev, t[i])
        k2 = equation(x_prev + (h/2) * k1, t[i] + (h/2))
        k3 = equation(x_prev + (h/2) * k2, t[i] + (h/2))
        k4 = equation(x_prev + h * k3, t[i] + h)

        x_next = x_prev + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x_prev = x_next
        runge_kutta_list.append(x_next)

    plt.plot(t, runge_kutta_list, 'm--', linewidth=1.5, label='Runge-Kutta approximation')
    return runge_kutta_list


def equation(x, t):
    dxdt = math.sin(x*math.pi*t)+math.pi*t*math.cos(math.pi*t)
    return dxdt


max_value = 200

t, h = np.linspace(0, 10, max_value, retstep=True)

solution = odeint(equation, 2, t)

plt.plot(t, solution, linewidth=1.5, label='Expected plot')

euler_list = euler_method(2, h, max_value)
heun_list = heun_method(2, h, max_value)
runge_kutta_list = runge_kutta_method(2, h, max_value)

plt.legend(loc='best')
plt.show()
