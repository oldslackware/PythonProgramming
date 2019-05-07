#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

x_data=np.linspace(0, 4, 50)
y = func(x_data, 2.5, 1.3, 0.5)

np.random.seed(2000)
y_noise = 0.2 * np.random.normal(size=x_data.size)

ydata = y + y_noise
plt.plot(x_data, ydata, 'b-', label='data')

popt, pcov = curve_fit(func, x_data, ydata)
print(popt)
plt.plot(x_data, func(x_data, *popt), 'r-',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

"Constrain the optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:"
popt, pcov = curve_fit(func, x_data, ydata, bounds=(0, [3., 1., 0.5]))
plt.plot(x_data, func(x_data, *popt), 'g--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
print(popt)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()