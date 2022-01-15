class student:

    school = 'MSMSV'

    def __init__(self, m1, m2 , m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.school
    @classmethod
    def info(cls):
        print("This is the Student class..in abc module")

s1 = student(12, 33, 44)
s2 = student(14, 45, 100)

print(s1.avg())
print(s2.avg())
print(student.get_school())
student.info()