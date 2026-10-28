import numpy as np
numbers = np.array([10, 20, 30, 40])

print(numbers + 5)
print(numbers - 5)
print(numbers * 2)
print(numbers / 10)

print("\n===========================\n")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a * b)

print("\n===========================\n")

prices = np.array([100, 200, 300])

discounted_prices = prices * 0.9

print(discounted_prices)