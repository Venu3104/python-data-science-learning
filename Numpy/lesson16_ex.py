import numpy as np

marks=np.array([80.0,90.0,np.nan,70.0,np.nan])
print(marks)
print(np.mean(marks))

print(np.isnan(marks))

print(np.nanmean(marks))

count=np.sum(np.isnan(marks))
print(count)

cleaned_marks=marks.copy()
cleaned_marks[np.isnan(cleaned_marks)]=0
print(cleaned_marks)

data = np.array([10.0, np.nan, 30.0, np.nan, 50.0])
print(np.isnan(data))

cleaned_data=data.copy()
cleaned_data[np.isnan(cleaned_data)]=25

print("Original data:",data)
print("Modfied_data:",cleaned_data)
