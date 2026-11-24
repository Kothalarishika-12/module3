from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def display(self):
        pass


class EmployeeDetails(Employee):

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.salary)


e = EmployeeDetails("janu", 101, 50000)

e.display()