#Perform matrix multiplication.(dot() or @).
import numpy as np
arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])
result_dot = np.dot(arr1, arr2)
result_at = arr1 @ arr2
print(result_dot)
print(result_at)