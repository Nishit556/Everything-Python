import numpy as np
import scipy.fft
from scipy.fft import fft, ifft
x = np.array([1, 2, 3, 4,])
y = fft(x)
print(y)
y = ifft(x)
print(y)
