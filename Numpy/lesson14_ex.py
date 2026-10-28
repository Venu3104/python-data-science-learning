import numpy as np

a=np.array([10,20,30,40])
b=np.array([10.2,20.5,30.7,40.9])

print(a.dtype)
print(b.dtype)

decimal_point=a.astype(float)
print(decimal_point)

integ=b.astype(int)
print(integ)
