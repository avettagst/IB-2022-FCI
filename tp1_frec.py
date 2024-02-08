from cProfile import label
from cmath import pi, sin
from mailbox import linesep
from turtle import width
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema as relex

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 9,
        }

c = 3e8 #[m/s]
fc = 1e9 #[GHz]
a = 1 #a1=a2
d = 200 #[m]
r = 80 #[m[]]


f = np.linspace(fc-2e6,fc+2e6,20000)

Td = 2*(d-r)/c
Wc = 0.5/Td

print(Wc)

canal = 4*(abs(a)*np.sin(2*pi*f*(d-r)/c))**2
canal = np.array(canal)

min = relex(canal,np.less)
max = relex(canal,np.greater)

print(min)
print(max)

plt.plot(f/1e6,canal,label = '|H(f;t)|$^2$')
plt.axhline(y=2,xmin=min[0][1]/len(f),xmax=max[0][2]/len(f), ls = '--', c = 'darkred')
plt.axvline(x=f[min[0][1]]/1e6, c = '0.5', ymax = 2.2/4.4, ls = '-.', linewidth = 0.5)
plt.axvline(x=f[max[0][2]]/1e6, c = '0.5', ymax = 4.2/4.4, ls = '-.', linewidth = 0.5)
plt.text(1000.02, 2.05, '$W_c$ = 625 kHz', fontdict=font)
plt.xlim(f[0]/1e6,f[-1]/1e6)
plt.ylim(-0.2,4.2)
plt.xlabel('Frecuencia [MHz]')
plt.ylabel('Respuesta del canal [u.a]')
plt.legend()
plt.show()






