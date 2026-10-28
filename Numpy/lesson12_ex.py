import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

combined=np.concatenate((a,b))
print(combined)

c=np.array([[1,2],[3,4]])
d=np.array([[5,6]])

vertical_stack=np.vstack((c,d))
print(vertical_stack)

e=np.array([[1],[2],[3]])
f=np.array([[4],[5],[6]])

horizontal_stack= np.hstack((e,f))
print(horizontal_stack)

g=np.array([10,20,30,40,50,60,70,80])
spiltted_array=np.split(g,4)
print(spiltted_array)

