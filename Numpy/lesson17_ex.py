import numpy as np

marks = np.array([75, 82, 91, 64, 88])

np.save("marks.npy", marks)

loaded_marks = np.load("marks.npy")

print(loaded_marks)

np.savetxt("marks.txt", marks, fmt="%d")

loaded_text = np.loadtxt("marks.txt", dtype=int)

print(loaded_text)

print(np.equal(loaded_marks,loaded_text))


data=np.array([12, 24, 36, 48, 60])

print(data)

np.save("data.npy",data)

loaded_data=np.load("data.npy")

print(loaded_data)

np.savetxt("data.txt",data,fmt="%d")

loaded_data_txt=np.loadtxt("data.txt",dtype=int)

print(loaded_data_txt)

print(np.equal(loaded_data,loaded_data_txt))