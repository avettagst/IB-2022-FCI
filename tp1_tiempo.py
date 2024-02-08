from cProfile import label
from cmath import pi, sin
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
v = 17 #[m/s] ~60km/h
fc = 1e9 #[GHz]
a = 1 #a1=a2
d = 200 #[m]
r0 = 40 #[m]

t = np.linspace(0,0.03,5000) #[s]
r = r0+v*t #[m]


Ds = 2*v*fc/c
Tc = 0.5/Ds

canal = 4*(abs(a)*np.sin(2*pi*fc*(d-r)/c))**2
canal = np.array(canal)

min = relex(canal,np.less)
max = relex(canal,np.greater)

print(min[0][0])
print(max[0][0])

print(t[min[0][0]]-t[max[0][0]])

plt.plot(1000*t,canal,label = '|H(f;t)|$^2$', c = 'g')
plt.axhline(y=2,xmin=max[0][1]/len(t),xmax=min[0][1]/len(t), ls = '--', c = 'darkred')
plt.axvline(x=t[max[0][1]]*1000, c = '0.5', ymax = 4.2/4.4, ls = '-.', linewidth = 0.5)
plt.axvline(x=t[min[0][1]]*1000, c = '0.5', ymax = 2.2/4.4, ls = '-.', linewidth = 0.5)
plt.xlim(1000*t[0],1000*t[-1])
plt.ylim(-0.2,4.2)
plt.text(10.55, 2.05, '$T_c$ = 4,41 ms', fontdict=font)
plt.xlabel('Tiempo [ms]')
plt.ylabel('Respuesta del canal [u.a]')
plt.legend()
plt.show()


