import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import random


xi = [-12.237, -9.712, -9.218, -7.235, -6.455, -4.869, -4.842, -4.407, -3.460, -2.527, -1.764, -1.711, -0.613, 0.252,
      0.363, 1.193, 1.720, 2.185, 3.379, 5.496, 6.511, 8.722, 10.292, 19.126]

yi = [-7.235, -1.711, 0.363, 3.379, 6.511, 8.722, 10.292, 19.126]

mean_xi = np.mean(xi)
sigma_xi = np.std(xi)
sigma_xi_3 = sigma_xi * 3

print(f'mean xi: {mean_xi}, standard deviation yi: {sigma_xi}, 3 sigma: {sigma_xi_3}')

list_xi = ['' for _ in range(1, 25)]

plt.figure()
plt.title('Initial set of measured temperatures with μ ± 3σ')
plt.scatter('', mean_xi, color='red', marker='_', s=500)
plt.scatter('', sigma_xi_3, color='red', marker='_', s=500)
plt.scatter('', -sigma_xi_3, color='red', marker='_', s=500)
plt.vlines('', -sigma_xi_3, sigma_xi_3, colors='red')
plt.scatter(list_xi, xi)

plt.figure()
plt.title('Normal distribution based on calculated mean and standard deviation\nfrom initial set')
distribution = np.linspace(mean_xi-sigma_xi_3, mean_xi+sigma_xi_3, 10000)
plt.plot(distribution, stats.norm.pdf(distribution, mean_xi, sigma_xi))

distribution_mean = np.mean(distribution)
distribution_sigma = np.std(distribution)
distribution_sigma_3 = distribution_sigma*3

distribution_list = ['' for _ in range(10000)]

plt.figure()
plt.title('10k samples generated on previous mean and standard deviation\nwith μ ± 3σ')
plt.scatter('', distribution_mean, color='red', marker='_', s=500)
plt.scatter('', distribution_sigma_3, color='red', marker='_', s=500)
plt.scatter('', -distribution_sigma_3, color='red', marker='_', s=500)
plt.vlines('', -distribution_sigma_3, distribution_sigma_3, colors='red')
plt.scatter(distribution_list, distribution)

new_measurements = [random.choice(distribution) for _ in range(24)]

new_measurements_mean = np.mean(new_measurements)
new_measurements_sigma = np.std(new_measurements)
new_measurements_sigma_3 = new_measurements_sigma*3

print(f'mean xi: {new_measurements_mean}, standard deviation yi: {new_measurements_sigma}, 3 sigma: '
      f'{new_measurements_sigma_3}')

plt.figure()
plt.title('New data set consisting of 24 samples randomly selected from previous\nnormal distribution with new μ ± 3σ')
plt.scatter('', new_measurements_mean, color='red', marker='_', s=500)
plt.scatter('', new_measurements_sigma_3, color='red', marker='_', s=500)
plt.scatter('', -new_measurements_sigma_3, color='red', marker='_', s=500)
plt.vlines('', -new_measurements_sigma_3, new_measurements_sigma_3, colors='red')
plt.scatter(list_xi, new_measurements)

plt.figure()
plt.title('Normal distribution based on calculated mean and standard deviation\nfrom new set of data')
distribution = np.linspace(new_measurements_mean-new_measurements_sigma_3,
                           new_measurements_mean+new_measurements_sigma_3, 10000)
plt.plot(distribution, stats.norm.pdf(distribution, new_measurements_mean, new_measurements_sigma))

plt.show()


