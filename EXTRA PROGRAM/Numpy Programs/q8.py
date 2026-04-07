#Sort elements in ascending and descending order.
import numpy as np
arr = np.array([50, 10, 40, 20, 30])
asc = np.sort(arr)
desc = np.sort(arr)[::-1]
print(asc)
print(desc)