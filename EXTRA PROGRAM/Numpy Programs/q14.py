#save and load a Numpy array.
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
np.save('my_array.npy', arr)
loaded_arr = np.load('my_array.npy')
print(loaded_arr)