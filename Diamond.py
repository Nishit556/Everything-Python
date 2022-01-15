num = int(input("enter num:"))
k=1
i=1
while i <= num:
    b=1
    while b <= num-i:
        print(" ", end=" ")
        b = b + 1
    j = 1
    while j <= k:
        print( k , end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1
i=1
k=num + 2
while (num > 0) :
    b = 1
    while b < i + 1:
        print(" ", end=" ")
        b = b + 1
    j = 1
    while (j <= ((num - 1) * 2) - 1):
        print(k , end=" ")
        j = j + 1
    print()
    num = num - 1
    i = i + 1
    k = k - 2
