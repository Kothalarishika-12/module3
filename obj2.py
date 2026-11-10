
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


e1 = Employee(101, "Ram", 25000)
e2 = Employee(102, "Sita", 30000)

e1.display()
e2.display()
