#!/usr/bin/python
import matplotlib.pyplot as plt
time = [18, 19, 20, 21]
beer = [0, 2, 4, 8]

plt.plot(time, beer)
plt.xlabel('Time (hr)')
plt.ylabel('Beer (nr)')
plt.show()
