class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


class Exam(Student):
    def __init__(self, name, roll_no, marks):
        super().__init__(name, roll_no)
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


e = Exam("Kethana", 101, 90)
e.display()