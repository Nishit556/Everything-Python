import numpy as np
from scipy import linalg
a = np.array([(1,2), (2,3)])
print(a)
b = linalg.inv(a)
print(b)