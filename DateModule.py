import time
print(time.time())
print(time.ctime(1612621003.080906))
a = (time.localtime())
b = (time.mktime(a))
print(b)
c = time.asctime(a)
print(c)
x = time.strftime("%m/%d/%y")
print(x)
import datetime
print(datetime.datetime(2021, 2, 6, 4, 50, 59, 546))
v = datetime.datetime.now()
print(v.year)