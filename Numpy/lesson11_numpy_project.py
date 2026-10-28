import numpy as np

marks = np.array([78, 45, 89, 62, 95, 34, 72, 88, 56, 91])

print("Student marks:", marks)

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Total:", np.sum(marks))
print("Standard deviation:", np.std(marks))


passed = marks[marks >= 50]
failed = marks[marks < 50]

print("Passed marks:", passed)
print("Failed marks:", failed)
print("Number passed:", np.sum(marks >= 50))
print("Number failed:", np.sum(marks < 50))

print("Ascending:", np.sort(marks))
print("Descending:", np.sort(marks)[::-1])

highest_index = np.argmax(marks)
lowest_index = np.argmin(marks)

print("Highest mark:", marks[highest_index])
print("Highest-scoring student index:", highest_index)

print("Lowest mark:", marks[lowest_index])
print("Lowest-scoring student index:", lowest_index)

rng = np.random.default_rng(42)

random_marks = rng.integers(0, 101, size=10)

print("Random marks:", random_marks)
print("Average:", np.mean(random_marks))
print("Passed:", random_marks[random_marks >= 50])


print("median :",np.median(marks))

above_80=marks[marks>=80]
print("Scored above 80:",above_80)
print(np.sum(marks>=80))

finding_marks=marks[(marks>=60) & (marks<=90)]
print("Finding all marks between 60 and 90:",finding_marks)
print("Count :", np.sum((marks>=60) & (marks<=90)))

Duplicate_marks=marks.copy()
Duplicate_marks[Duplicate_marks<=50]=50
print("Duplicate_marks:",Duplicate_marks)


reshaped_marks=marks.reshape(2,5)
print("Reshaping :",marks.reshape(2,5))
print("Averages of ech row",reshaped_marks.mean(axis=1))

print("Unique values:", np.unique(marks))