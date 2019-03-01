'''import numpy as np

a = np.array([[10**-9,1],[1,1]])
b = np.array([1,2])
m21 = a[1][0] / a[0][0]
a[1][1] = 1 - m21*1
b[1] = 2 - m21 *1
x1 = b[1]/a[1][1]
x2 = x1*a[0][1]
print(x1)
print(x2)
print(a[1][1])
print(b[1])'''

c= 1
a=b=c
print(a)
print(b)