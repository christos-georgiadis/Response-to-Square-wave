import numpy as np
from math import *
from matplotlib import pyplot as plt


z = 0.01
htta = [i for i in np.arange(0,2, 0.001)]
        
    
x_rms = []

for h in htta:
    x_squared = 0
    
    for n in np.arange(1,20,2):
        a0 = 1/2
        c1 = 1-n**2*h**2
        c2 = 2*z*n*h
        an = 1/(n*sqrt(c1**2+c2**2))*2/pi
        bn = 0
        x_squared += an**2 + bn**2
    
    x_squared = a0 + 1/2*x_squared
    x_rms.append(sqrt(x_squared))

plt.plot(htta,x_rms, color='black', linewidth = 0.5)
plt.savefig('multiple_resonants.png', dpi=300)
plt.xlim([0, 2])
plt.ylim([0, 25])
plt.show()