class Person:
    sex = "M"
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def info(self):
        print(self.name, self.age, self.country)

    def get_sex(cls):
        print(cls.sex)


p1 = Person("John", 21, "India")
p1.info()