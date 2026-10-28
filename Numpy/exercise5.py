import numpy as np

sales = np.array([1200, 1500, 900, 1800, 1100])

print(sales.sum())
print(sales.mean())
print(sales.min())
print(sales.max())
print(sales.std())


sales =np.array([[100, 200, 300], 
         [400, 500, 600], 
         [700, 800, 900],
         [1000, 1100, 1200]])

print(sales.sum(axis=0))  # Sum along columns
print(sales.sum(axis=1))  # Sum along rows