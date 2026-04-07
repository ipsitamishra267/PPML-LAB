#extract elements greater than 10.
import numpy as np
arr = np.array([5, 12, 7, 18, 3, 25])
greater_than_10 = arr[arr > 10]
print(greater_than_10)