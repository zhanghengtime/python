import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.32,0.34,0.36])
y = np.array([0.314567,0.333487,0.352274])
a = np.arange(0, 4, 0.0005)
b = np.arange(0, 4, 0.0005)
c = np.array([0.3367])
plt.plot(a, np.sin(a), 'r--')
plt.plot(b, y[0]*(b-x[1])*(b-x[2])/(x[0]-x[1])/(x[0]-x[2]) + y[1]*(b-x[0])*(b-x[2])/(x[1]-x[0])/(x[1]-x[2]) + y[2]*(b-x[0])*(b-x[1])/(x[2]-x[0])/(x[2]-x[1]), 'k')
#plt.plot(c, y[0]+ (y[1]-y[0])/(x[1]-x[0])*(c - x[0]), 'rX')
#plt.plot(c, y[0]*(c-x[1])*(c-x[2])/(x[0]-x[1])/(x[0]-x[2]) + y[1]*(c-x[0])*(c-x[2])/(x[1]-x[0])/(x[1]-x[2]) + y[2]*(c-x[0])*(c-x[1])/(x[2]-x[0])/(x[2]-x[1]), 'mX')
plt.plot([0.32,0.34,0.36],[0.314567,0.333487,0.352274], 'gP')
plt.xlabel('横轴: x', fontproperties='SimHei', fontsize=20, color='green')
plt.ylabel('纵轴: y', fontproperties='SimHei', fontsize=20)
plt.title(r'$y=sin(x)$', fontproperties='SimHei', fontsize=20)
#plt.axis([0, np.pi,0,1])
plt.grid(True)
plt.show()
