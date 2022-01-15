numbers = [3, 5 ,6 , 4, 7 , 4, 33, 6 , 7, 8 , 9]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(111)
numbers2 = numbers.copy()
print(numbers2)
list = []
for number in numbers:
    if number not in list:
        list.append(number)
print(list)
