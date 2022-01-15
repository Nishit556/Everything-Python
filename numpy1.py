import numpy as np
import sys
a = np.array([(1, 2, 3), (2, 3, 4), (5, 4, 7)])
print(a)
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)
print(a[0:2, 1])
print(a.max())
print(a.min())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.T) # Transpose
print(a.flat)
for item in a.flat:
    print(item)
print(a.nbytes)
print(np.sqrt(a))
#print(a.reshape())
x = np.linspace(1, 3 ,5) #Gives 5 values between 1 to 3
print(x)
# axis = 1 rows
# axis = 0 columns
print(np.where(a>5))
print(np.count_nonzero(a))
print(np.nonzero(a))

py_ar = [0, 4, 5, 6]
np_ar = np.array(py_ar)
print(sys.getsizeof(1) * len(py_ar))
print(np_ar.itemsize * np_ar.size)
print(a.squeeze())
