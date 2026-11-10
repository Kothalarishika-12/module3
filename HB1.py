class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


class Sports(Person):
    def __init__(self, name, sports_score):
        super().__init__(name)
        self.sports_score = sports_score


class Result(Student, Sports):
    def __init__(self, name, marks, sports_score):
        Student.__init__(self, name, marks)
        Sports.__init__(self, name, sports_score)

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Sports Score:", self.sports_score)


r = Result("Ravi", 85, 90)
r.display()