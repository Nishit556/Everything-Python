import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(np.cos(2*np.pi*t))
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211) # 211 means we have 2 plots, horizontly we have one plot present and at that vertical position this will be our first plot
plt.plot(t1, f(t1),'k^', t2, f(t2))
plt.subplot(212)
plt.plot(t2, np.sin(np.pi*t2))
plt.show()
