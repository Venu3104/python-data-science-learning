import numpy as np

a=np.array([5,10,15,20,25])
b=a[1:3]
print(b)

b[0]=100
print(b)
print(a)

d=np.array([5,10,15,20,25])
c=d.copy()
c=a[1:3]
c[0]=100

print(d)
print(c)
