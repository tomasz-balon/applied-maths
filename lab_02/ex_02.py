import sys
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def evaluate_alcohol(U, t, k1, k2, k3, I, M):
    x, y = U

    dxdt = I - (k1 * x)
    dydt = (k2 * x) - ((k3 * y) / (y + M))

    return [dxdt, dydt]


if __name__ == '__main__':
    W = int(input('How much do you weigh [kg]: '))
    sex = input('"M" for man "W" for woman: ')
    n = int(input('How many drinks have you had: '))
    time = int(input('Time span [hrs]: '))
    M = 0.005

    if sex == 'M':
        I_param = (n * 14 * 100) / (0.82 * W * 1000)
        k3 = (8 * 100) / (0.82 * W * 1000)
    elif sex == 'W':
        I_param = (n * 14 * 100) / (0.67 * W * 1000)
        k3 = (8 * 100) / (0.67 * W * 1000)
    else:
        print('Something went wrong.')
        sys.exit(1)

    time_span = np.linspace(0, time, 1000)

    empty_stomach_constant_drinking_param = [0, 0]
    empty_stomach_sudden_drinking_param = [I_param, 0]
    full_stomach_constant_drinking_param = [0, 0]
    full_stomach_sudden_drinking_param = [I_param, 0]

    empty_stomach_constant_drinking = odeint(evaluate_alcohol, empty_stomach_constant_drinking_param,
                                             time_span, args=(6, 6, k3, I_param, M))

    empty_stomach_sudden_drinking = odeint(evaluate_alcohol, empty_stomach_sudden_drinking_param,
                                           time_span, args=(6, 6, k3, 0, M))

    full_stomach_constant_drinking = odeint(evaluate_alcohol, full_stomach_constant_drinking_param,
                                            time_span, args=(6, 3, k3, I_param, M))

    full_stomach_sudden_drinking = odeint(evaluate_alcohol, full_stomach_sudden_drinking_param,
                                          time_span, args=(6, 3, k3, 0, M))

    plt.figure()
    plt.title('Empty stomach constant drinking')
    plt.plot(time_span, empty_stomach_constant_drinking[:, 0], label='Digestive system')
    plt.plot(time_span, empty_stomach_constant_drinking[:, 1], label='Circulatory system')
    plt.legend(loc='best')
    plt.xlabel('Time [hrs]')
    plt.ylabel('BAL [g/100ml]')
    plt.grid()

    plt.figure()
    plt.title('Empty stomach sudden drinking')
    plt.plot(time_span, empty_stomach_sudden_drinking[:, 0], label='Digestive system')
    plt.plot(time_span, empty_stomach_sudden_drinking[:, 1], label='Circulatory system')
    plt.legend(loc='best')
    plt.xlabel('Time [hrs]')
    plt.ylabel('BAL [g/100ml]')
    plt.grid()

    plt.figure()
    plt.title('Full stomach constant drinking')
    plt.plot(time_span, full_stomach_constant_drinking[:, 0], label='Digestive system')
    plt.plot(time_span, full_stomach_constant_drinking[:, 1], label='Circulatory system')
    plt.legend(loc='best')
    plt.xlabel('Time [hrs]')
    plt.ylabel('BAL [g/100ml]')
    plt.grid()

    plt.figure()
    plt.title('Full stomach sudden drinking')
    plt.plot(time_span, full_stomach_sudden_drinking[:, 0], label='Digestive system')
    plt.plot(time_span, full_stomach_sudden_drinking[:, 1], label='Circulatory system')
    plt.legend(loc='best')
    plt.xlabel('Time [hrs]')
    plt.ylabel('BAL [g/100ml]')
    plt.grid()
    plt.show()
