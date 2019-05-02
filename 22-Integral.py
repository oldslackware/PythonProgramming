import scipy.integrate
from numpy import log
"Integral of log 3x between 2 and 3"
f=lambda x:log(3*x)
i=scipy.integrate.quad(f,2,3)
"first value result second value error of integral(+c)"
print (i)