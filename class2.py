
class Employee:
    emp_id = 101
    name = "charan"
    salary = 250000
    dept= "IT"

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee Department:", self.dept)

e1 = Employee()
e1.display()
