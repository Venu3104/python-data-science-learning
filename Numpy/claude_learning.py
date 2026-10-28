import numpy as np

# print(np.zeros((2,3)))
# print(np.ones((3,4)))
# print(np.eye(3))

# print(np.empty((2,2)))
# print(np.arange(0,10,2))
# print(np.linspace(0,1,5))
# print(np.logspace(0,1,4))


a = np.array([[1, 2], [3, 4]])
# print(np.zeros_like(a))            # same shape/dtype as a
# print(np.arange(12).reshape(3, 4))

xx, yy = np.meshgrid(np.arange(3), np.arange(4))
print(xx)
print(yy)

a = np.ones((5, 5), dtype=int)
a[1:-1, 1:-1] = 0
print(a)

