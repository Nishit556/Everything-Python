import numpy as np
a = np.array([(1, 2, 3), (2, 3, 4), (5, 4, 7)])
b = np.array([(3, 2, 3), (2, 3, 4), (8, 4, 7)])
print(a + b)
print(a * b)
print(a/b)
print(np.vstack(a))
print(a.ravel())