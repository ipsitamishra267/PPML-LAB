#Generate random numbers.
import numpy as np
rand_int = np.random.randint(1, 101, size=5)
rand_float = np.random.rand(5)
rand_normal = np.random.randn(5)
print(rand_int)
print(rand_float)
print(rand_normal)