import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pylab as plb
import numpy as np
data = plb.loadtxt('my_data.txt')
x = data[:,0]
y= data[:,1]
def line(x, a):
  return a* x**2
popt, pcov = curve_fit(line, x, y)
print(popt[0])
plt.plot(x,y,'o')
xfine = np.linspace(0., 6., 10)  # define values to plot the function for
plt.plot(xfine, line(xfine, popt[0],), 'r-')


plt.show()