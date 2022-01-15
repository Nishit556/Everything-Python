import numpy as np
import time

SIZE = 100000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.array(SIZE)
A2 = np.array(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(L1, L2)]
print((time.time() - start) * 1000)
start = time.time()
result = A1 + A2
print((time.time() - start) * 1000)