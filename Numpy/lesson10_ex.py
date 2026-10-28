import numpy as np

rng=np.random.default_rng(42)
numbers=rng.random(5)
print(numbers)

rng1=np.random.default_rng()
numbers1=rng1.random(10)
print(numbers1)

rng2=np.random.default_rng()
numbers2=rng2.integers(1,51,size=8)
print(numbers2)

rng3=np.random.default_rng()
numbers3=rng3.integers(10,100,size=9)
print(numbers3.reshape(3,3))

rng4=np.random.default_rng()
numbers4=rng4.uniform(5,15,5)
print(numbers4)


values=[10, 20, 30, 40, 50, 60]
rng5=np.random.default_rng(42)
selected_values=rng5.choice(values,size=5, replace=False)
print(selected_values)

array_values=np.array([1, 2, 3, 4, 5, 6])
shuffled_values=rng.permutation(array_values)
print(shuffled_values)
print(array_values)

rng10=np.random.default_rng(123)
rng11=np.random.default_rng(123)
print(rng10.random(5))
print(rng11.random(5))