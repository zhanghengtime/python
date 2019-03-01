'''import numpy as np

x = np.array([0,0,0])
x = x.reshape(3,1)
b = np.array([[0,-2/5.0,-1/5.0],[(1)/4.0,0,-1/2.0],[-1/5.0,(3)/10.0,0]])
b = b.reshape(3,3)
c = np.array([[0,-2/5.0,-1/5.0],[0,-1/10.0,-11/20.0],[0,1/20.0,-1/8.0]])
f = np.array([-12/5.0,5,3/10.0])
g = np.array([-12/5.0,22/5.0,21/10.0])
g = g.reshape(3,1)
f = f.reshape(3,1)
xk = b.dot(x) + f
xg = c.dot(x) + g
i=0
while(np.linalg.norm((xg-x),ord=np.inf)>=10**(-4)):
    x = xg
    xg = c.dot(x) + g
    i=i+1
print(xg)
print(i)'''

from numpy import *
import operator
np = array([[1,2,3],[4,5,6],[7,8,9]])
print(np)
ns = np[0:2,0:2]
print(ns)