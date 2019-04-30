#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 2 * np.pi, 0.1)
y=np.sin(x)
y2=np.cos(x)
y3=y/2
y4=y2/2
fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)
#Title of figure
fig.suptitle("SUBPLOTS SAMPLES", fontsize=16)
axes[0][0].set_title("Sin(x)")
axes[0][0].plot(x,y)
axes[0][1].set_title("Cos(x)")
axes[0][1].plot(x,y2)
axes[1][0].set_title("Sin(x)/2")
axes[1][0].plot(x,y3)
axes[1][1].set_title("Cos(x)/2")
axes[1][1].plot(x,y4)
plt.savefig("PlotPyhton.png")
plt.show()