import numpy as np

temperatures = np.array([22, 35, 18, 40, 29, 15, 33, 26])

print(temperatures>30)
print(temperatures[temperatures>30])
print("\n=============\n")

print(temperatures<=22)
print(temperatures[temperatures<=22])
print("\n=============\n")

print((temperatures>=20) & (temperatures<=35))
print(temperatures[(temperatures>=20) & (temperatures<=35)])
print("\n=============\n")

print((temperatures<20) | (temperatures>35))
print(temperatures[(temperatures<20) | (temperatures>35)])
print("\n=============\n")

count=np.sum(temperatures>25)
print(count)

temperatures[temperatures<20]=20
print(temperatures)