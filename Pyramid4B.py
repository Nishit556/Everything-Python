n = int(input("Enter number of rows:"))
i=1
k=n
while (n > 0) :
    b = 1
    while b < i :
        print("  ", end="")
        b = b + 1
    j = 1
    while (j <= (n * 2) - 1):
        print(k , end=" ")
        j = j + 1
    print()
    n = n - 1
    i = i + 1
    k = k - 1
