#Convert a 1D array into a 2D array.
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = arr1.reshape(2, 3)
print(arr1)
print(arr2)
print(arr2.shape)
print(arr2.ndim)