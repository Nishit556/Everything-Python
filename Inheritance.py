class A:
    def __init__(self):
        print("Fuck Modi A")
    def feature1(self):
        print("feature 1A is working")
    def feature2(self):
        print("feature 2 is working")
class B():
    def __init__(self):
        print("Fuck Modi B")

    def feature1(self):
        print("feature 1B is working")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
    def feature5(self):
        print("feature 5 is working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("Fuck Modi C")



b1 = C()
b2 = C()
b1.feature1()
b2.feature4()


