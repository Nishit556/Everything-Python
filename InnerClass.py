class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student('Navin', 2)
s2 = student('Jenny', 3)

s1.show()



