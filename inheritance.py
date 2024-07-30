class Animal:
    def walk(self):
        print("I am walking")


class Bird(Animal):
    def fly(self):
        print("I am flying")

b1 = Bird()

b1.walk()
b1.fly()