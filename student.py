class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.lap_top = self.LapTop()

    def show(self):
        print(self.first_name)
        self.lap_top.show()

    class LapTop:
        def __init__(self):
            self.mark = "HP"
            self.cpu = 64

        def show(self):
            print(self.mark, self.cpu)


s1 = Student("John", "Doe")

s1.show()


