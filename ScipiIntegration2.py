import scipy.integrate
def f(x):
    return x**2
i = scipy.integrate.quad(f, 0, 2)
print(i)