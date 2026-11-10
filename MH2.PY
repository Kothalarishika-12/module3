class Student:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Student Name:", self.name)


class Sports:
    def __init__(self, sport):
        self.sport = sport

    def display_sport(self):
        print("Sport:", self.sport)


class Result(Student, Sports):
    def __init__(self, name, sport):
        Student.__init__(self, name)
        Sports.__init__(self, sport)


r = Result("Kethana", "Badminton")
r.display_name()
r.display_sport()