class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.lap_top = self.LapTop()

    class LapTop:
        def __init__(self):
            self.mark = "HP"
            self.cpu = 64


s1 = Student("John", "Doe")

print(s1.lap_top.mark)
