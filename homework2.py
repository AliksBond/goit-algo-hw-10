import numpy as np

def f(x):
    return x ** 2

a, b = 0, 2
N = 100000

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

points_under_curve = np.sum(y_random <= f(x_random))
integral_monte_carlo = (b - a) * f(b) * points_under_curve / N

print("Monte Carlo result:", integral_monte_carlo)



""" перевірка результату """

import scipy.integrate as spi

def f(x):
    return x ** 2

a, b = 0, 2
result, error = spi.quad(f, a, b)

print("Quad result:", result)
print("Error:", error)





