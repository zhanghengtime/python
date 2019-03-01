from numpy import *

t = dtype([('name', str_, 40), ('numitems', int32), ('price', float32)])
itemz = array([('DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
c = arange(27).reshape(3, 3, 3)
print(dsplit(c, 3))