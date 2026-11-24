from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def display(self):
        pass


class StudentDetails(Student):

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Student Roll Number:", self.roll_no)
        print("Student Marks:", self.marks)


s = StudentDetails("Rishi", 12, 95)

s.display()