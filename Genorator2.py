def new(dict):
    for x, y in dict.items():
        yield x,y
a = {1:"Hi", 2:"Welcome"}
b = new(a)
print(b)
print(next(b))

def myfunc(i):
    while i<=5:
        yield i
        i = i + 1
j = myfunc(3)
print(next(j))
print(next(j))

def ex():
    n=3
    yield n
    n = n*n
    yield n
v = ex()
print(next(v))
print(next(v))