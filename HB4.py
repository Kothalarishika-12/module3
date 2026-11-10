class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Intern(Employee, Student):
    def __init__(self, name, age, emp_id, roll_no):
        Employee.__init__(self, name, age, emp_id)
        Student.__init__(self, name, age, roll_no)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Roll Number:", self.roll_no)


i = Intern("Sita", 21, 501, 101)
i.display()