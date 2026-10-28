import numpy as np
numbers=np.array([5,10,15,20,25])

print(numbers[1])
print(numbers[1:4])
print(numbers[::2])

print("\n===========================\n")

marks = np.array([
    [85, 90, 95],
    [70, 80, 75],
    [60, 65, 70]])

print(marks[0, 1])
print(marks[1, 2])
print(marks[0])