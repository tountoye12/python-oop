class Animal:
    def walk(self):
        print("I am walking")


class Bird(Animal):
    def fly(self):
        print("I am flying")


# b1 = Bird()
#
# b1.walk()
# b1.fly()

class A:
    def __init__(self):
        print("In A")

    def future_1(self):
        print("Future 1 in A")


class B:
    def __init__(self):
        print("In B")

    def future_1(self):
        print("Future 1 in B")


# MRO ==> Method resolution order
class C(B, A):
    def __init__(self):
        print("In C")
        super().__init__()  # In C In B


c1 = C()
