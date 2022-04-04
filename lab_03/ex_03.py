import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


def numerical(x, t, r, gamma):
    dxdt = (r * x) - (gamma * (x ** 2))
    return dxdt


def discrete(x_0, r, K, lambda_param):
    x_prev = x_0
    result = [x_prev]
    x = [0]

    for i in range(1000):
        x_next = lambda_param * x_prev * (1 - x_prev)
        # x_next = x_prev + (r * x_prev * (1 - (x_prev/K) - (x_prev/(r*K))))
        # x_next = x_prev + (r * x_prev * (1 - (x_prev/K)))
        x_prev = x_next
        result.append(x_next)
        x.append(i)

    plt.figure()
    plt.title(f'Discrete solution, λ={lambda_param}')
    plt.scatter(x, result)


def logistic(lambda_logistic_param, x):
    return lambda_logistic_param * x * (1 - x)


def bifurcation():
    samples_size = 10000
    lambda_bifurcation = np.linspace(0.001, 4, samples_size)
    x = np.ones(samples_size) * 0.001
    result_list = []
    lambda_list = []

    plt.figure()

    for i in range(1000):
        x = logistic(lambda_bifurcation, x)

        if i >= 900:
            plt.plot(lambda_bifurcation, x, ',', alpha=0.25)

    plt.title('Bifurcation')
    plt.xlabel('λ')
    plt.ylabel(r'$x_{k}$')
    plt.scatter(lambda_list, result_list)


if __name__ == '__main__':
    t = np.linspace(0, 100, 10000)
    x0 = 0.001
    r_arr = [0.1, 0.2, 0.4, 1.4, 2.2, 2.9]
    K = 1000

    for r in r_arr:
        gamma = 0.1
        gamma2 = 0.4
        gamma3 = 1.1
        gamma4 = 1.4

        solution = odeint(numerical, x0, t, args=(r, gamma))
        solution2 = odeint(numerical, x0, t, args=(r, gamma2))
        solution3 = odeint(numerical, x0, t, args=(r, gamma3))
        solution4 = odeint(numerical, x0, t, args=(r, gamma4))
        lambda_param = 1 + r
        discrete(x0, r, K, lambda_param)

        plt.figure()
        plt.title(f'Numerical solution, r={r}')
        plt.plot(t, solution[:, 0], label=' \u03B3 = 0.1')
        plt.plot(t, solution2[:, 0], label=' \u03B3 = 0.4')
        plt.plot(t, solution3[:, 0], label=' \u03B3 = 1.1')
        plt.plot(t, solution4[:, 0], label=' \u03B3 = 1.4')
        plt.legend(loc='best')

    bifurcation()

    plt.show()
