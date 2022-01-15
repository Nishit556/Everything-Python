def ex():
    n=3
    yield n
    n = n*n
    yield n
    n = print("Jatin Fucks Minors")
    yield n
v = ex()
for x in v:
    print(x)