import numpy as np
numbers=np.array([10, 20, 30, 40, 50, 60])
print(numbers.shape)
print(numbers.reshape(2,3))
print("\n=============\n")
print(numbers.reshape(3,2))
print("\n=============\n")
print(numbers.reshape(2,-1))
print("\n=============\n")
print(numbers.reshape(3,-1))


matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
flat=matrix.flatten()

print(flat)

print(matrix.T)
