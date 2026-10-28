import numpy as np

scores = np.array([85, 60, 90, 60, 45, 85, 72, 30])

print(np.sort(scores))

descending=np.sort(scores)[::-1]
print(descending)

unique_scores=np.unique(scores)
print(unique_scores)

values, count =np.unique(scores, return_counts=True)
print(values)
print(count)


indices=np.where(scores>70)
print(indices)

minimum=np.min(scores)
min_idx=np.argmin(scores)
print("minimum:", minimum)
print("index of minimum:", min_idx)

maximum=np.max(scores)
max_idx=np.argmax(scores)
print("maximum:", maximum)
print("index of maximum:", max_idx)

results=np.where(scores>=50, "Pass","Fail")
print(results)

