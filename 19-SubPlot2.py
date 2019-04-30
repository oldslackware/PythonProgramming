#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 2 * np.pi, 0.1)
z=np.arange(0, 4 * np.pi, 0.1)
y=np.sin(x)
zf=np.sin(z)
plt.figure(1)
plt.title("Sin(x)")
#Lineare
plt.subplot(2,2,1)
plt.plot(x,y)
plt.yscale("linear")
plt.ylabel("Scale Linear")
plt.title("Sin(x) Linear Scale")
plt.grid()
#Logaritmica
plt.subplot(2,2,2)
plt.plot(x,y)
plt.yscale("log")
plt.ylabel("Scale Log")
plt.title("Sin(x) Scala Log")
plt.grid()
#SEMILogaritmica
plt.subplot(2,2,3)
plt.plot(x,y-y.mean())
plt.yscale("symlog",linthreshy=0.01 )
plt.ylabel("Scale SEMILog")
plt.title("Sin(x) Scale SemiLog")
plt.grid()
#Linear in 4 pi
plt.subplot(2,2,4)
plt.plot(z,zf)
plt.yscale("linear")
plt.ylabel("Scale Linear")
plt.title("Sin(x) in 4 pi")
plt.grid()
plt.show()