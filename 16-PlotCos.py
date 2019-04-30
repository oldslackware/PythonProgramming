#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 2 * np.pi, 0.1)
y=np.cos(x)
z=np.sin(x)
plt.title('Cosin figure')
plt.stem(x,y, 'r', )
plt.stem(x,z, 'r')
plt.plot(x,y,x,z,y,x)
plt.show()