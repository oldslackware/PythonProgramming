import matplotlib.pyplot as plt
import numpy as np
"Plot the function x2+3x-3 in the range -1 4 with 100 dots"
x=np.linspace(-10, 4, 100)
y=x**2+3*x-3
plt.plot(x,y)
plt.show()