##lambda within filter()
A_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(filter(lambda a:(a % 2 == 1),A_list)) #SYNTAX filter(function,interables)
print(A_list)
print(new_list)

##lambda within map()
B_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p = list(map(lambda a:(a/3 != 2),B_list))
print(B_list)
print(p)

##lambda with reduce()
from functools import reduce
w = reduce(lambda a,b: a+b,[23,56,43,98,1])
print(w)

##lambda for algebra

#linear equations
s = lambda a: a*a
print(s(4))

#3x+4y
d=lambda x,y: 3*x + 4*y
print(d(2,3))

#quadratic Equation
#(a+b)^2
x = lambda a,b: (a + b)**2
print(x(3,3))

