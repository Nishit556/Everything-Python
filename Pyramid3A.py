num = int(input("Enter number of rows:"))
k=1
i=1
while i <= num:
    b=1
    while b <= num-i:
        print(" ", end=" ")
        b = b + 1
    j = 1
    while j <= k:
        print("*", end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1
