import numpy as np

marks = np.array([78, 45, 89, 62, 95, 34, 72, 88, 56, 91])

# Print the marks
# Print the average
# Print the median
# Print the highest and lowest marks

print(marks)
print(np.mean(marks))
print(np.median(marks))
print(np.max(marks))
print(np.min(marks))

# Create a passed array containing marks greater than or equal to 50.

passed=marks[marks>=50]
print(passed)



# Create a failed array containing marks below 50.
failed=marks[marks<50]
print(failed)



# Print both arrays.



# Print the number of students who passed and failed.
passed_count=np.sum(marks>=50)
print(passed_count)

failed_count=np.sum(marks<50)
print(failed_count)


# Find all marks 80 or above.
print(marks[marks>=80])



# Count how many students scored 80 or above.

print(np.sum(marks>=80))

# Display all marks in ascending order.
print(np.sort(marks))



# Display all marks in descending order.
print(np.sort(marks)[::-1])

# Find the index of the highest mark using np.argmax().
maxvalue=np.argmax(marks)

# Find the index of the lowest mark using np.argmin().
minvalue=np.argmin(marks)



# Print both indices.
print(maxvalue)
print(minvalue)


# Use those indices to print the corresponding marks.
print(marks[maxvalue])
print(marks[minvalue])

# Calculate the standard deviation using np.std(marks).
stand_dev=np.std(marks)
print(stand_dev)


# Reshape the 10 marks into a 2D array with 2 rows and 5 columns.
reshaping_array=marks.reshape(2,5)
print(reshaping_array)



# Calculate the average for each row using axis=1.
averages=reshaping_array.mean(axis=1)



# Print both row averages.
print(averages)

# Find all unique marks using np.unique().
print(np.unique(marks))


# Create a copy of marks.
copying_marks=marks.copy()



# Replace every mark below 50 with 50 in the copy.
copying_marks[marks<50]=50




# Print the original array and the modified copy to confirm that the original remains unchanged.
print("original array: ",marks)
print("duplicate array: ",copying_marks)

# Save the array to student_marks.npy using np.save().
np.save("student_marks.npy",marks)


# Load it into a new variable using np.load().
loaded_marks=np.load("student_marks.npy")



# Print the loaded array.
print(loaded_marks)



# Verify that the original and loaded arrays are identical using np.array_equal().
equality=np.equal(marks,loaded_marks)



# Print the comparison result.
print(equality)

# Calculate the number of students who passed (marks >= 50).
passed_count = np.sum(marks >= 50)



# Calculate the pass percentage.
pass_percentage = (passed_count / marks.size) * 100



# Display a progress bar where each # represents 10 percentage points.
progress_bar="#"*passed_count


# Print the pass percentage and progress bar.
print(pass_percentage)
print(progress_bar)