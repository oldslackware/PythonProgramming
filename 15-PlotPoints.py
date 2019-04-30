#!/usr/bin/python
import matplotlib.pyplot as plt
plt.plot([0, 3, 6, 9], [0, 5, 10, 15], 'ro')
plt.axis([0,10,0,20])
plt.xlabel('x')
plt.ylabel('y')
plt.show()