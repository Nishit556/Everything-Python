list_1 = [1, 2, 3, 4]
list_2 = [2, 5, 4, 6]
x = list(map(lambda a,b: (a * b) , list_1, list_2))
print(x)