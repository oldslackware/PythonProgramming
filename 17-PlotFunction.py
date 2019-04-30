#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-x) * np.cos(2*np.pi*x)

x1=np.arange(0.0,10.0,0.01)
plt.annotate('average', xy=(2, 0.1), xytext=(4, 0.5),fontsize=40, color="green",
            arrowprops=dict(facecolor='red', shrink=0.1),)
plt.plot(x1,f(x1), 'bo')
plt.grid()
plt.show()