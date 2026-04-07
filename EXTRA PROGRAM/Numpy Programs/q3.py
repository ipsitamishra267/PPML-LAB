#create arrays using zeros(),ones(),and empty().
import numpy as np

arr1 = np.zeros((2, 3))
print(arr1)
print(arr1.shape)
print(arr1.ndim)

arr2 = np.ones((3, 2))
print(arr2)
print(arr2.shape)
print(arr2.ndim)

arr3 = np.empty((2, 2))
print(arr3)
print(arr3.shape)
print(arr3.ndim)