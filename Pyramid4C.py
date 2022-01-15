num = int(input("enter num:"))
i=1
while (num > 0) :
    b = 1
    while b < i :
        print("  ", end="")
        b = b + 1
    j = 1
    while (j <= (num * 2) - 1):
        print(i , end=" ")
        j = j + 1
    print()
    num = num - 1
    i = i + 1
