class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


s = Student("Ravi", 20, 101)
s.display()

print()

t = Teacher("Sita", 35, "Python")
t.display()