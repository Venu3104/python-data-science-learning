import numpy as np

numbers = np.array([5, 10, 15, 20])
print(numbers + 10)
print(numbers*3)

numbers2 = np.array([1, 2, 3, 4])
print(numbers + numbers2)

print("\n===========================\n")

print((numbers+numbers2).mean())