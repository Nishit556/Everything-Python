#integration
import scipy
from scipy import integrate, special
i = scipy.integrate.quad(lambda x: special.exp10(x), 0, 1)
print(i)
e = lambda x,y: x*y**2
f = lambda x: 1
g = lambda x: -1
x = integrate.dblquad(e, 0, 2, f, g)
print(x)
