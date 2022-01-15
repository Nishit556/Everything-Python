def A(x):
    return(lambda y:x+y)
t=A(4)
print(t(8))
u=A(7)
print(u(5))
