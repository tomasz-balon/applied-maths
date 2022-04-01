import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


def numerical(x, t, r, gamma):
    dxdt = (r*x) - (gamma * (x**2))
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


def bifurcation():
    lambda_bifurcation = np.linspace(0.001, 4, 4000)
    x_0 = 0.001
    x_prev = 0.5
    X_list = []
    Y_list = []

    for lambda_bifurcation_param in lambda_bifurcation:
        X_list.append(lambda_bifurcation_param)
        x_next = lambda_bifurcation_param * x_prev * (1 - x_prev)
        x_prev = x_next
        Y_list.append(x_next)

    plt.figure()
    plt.title('Bifurcation')
    plt.scatter(X_list, Y_list)


if __name__ == '__main__':
    t = np.linspace(0, 100, 10000)
    # x0 = 100
    x0 = 0.001
    # r_arr = [0.2, 0.8, 2.2, 3.0, 3.4, 3.8, 4.0]
    r_arr = [0.2, 0.8, 2.2, 3.0]
    K = 1000

    # for r in r_arr:
    #     gamma = (1 + r) / K
    #     # gamma = r / K
    #     solution = odeint(numerical, x0, t, args=(r, gamma))
    #
    #     lambda_param = 1 + r
    #     discrete(x0, r, K, lambda_param)
    #
    #     plt.figure()
    #     plt.title(f'Numerical solution, r={r}')
    #     plt.plot(t, solution[:, 0])

    bifurcation()

    plt.show()
