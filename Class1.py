class computer:
    def __init__(self):
        self.name = "Modi"
        self.age = 74
        print("fuck Modi")
    def update(self):
        self.age = 30
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()
c1.name = "rashi"
c1.age = 12
c2.update()

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

if c1.compare(c2):
    print("They are the fucking same age")
else:
    print("They are not the same age")