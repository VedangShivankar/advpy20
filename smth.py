import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

#for row in a.flatten():
 #   print(cell)

for x in np.nditer(a,order='F',flags=['external_loop']):
    print(x)

for x in np.nditer(a,op_flags=['readwrite']):
    x[...]= x*x
    print(x)

d = np.arange(3,15,4).reshape(3,1)
print(d)

for x,y in np.nditer([a,b]):
    print(x,y)
