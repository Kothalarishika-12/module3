from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def display(self):
        pass


class CalculatorDetails(Calculator):

    def __init__(self, Add, sub, mul, div):
        self.Add = Add
        self.sub = sub
        self.mul = mul
        self.div = div

    def display(self):
        print("Addition:", self.Add)
        print("Subtraction:", self.sub)
        print("Multiplication:", self.mul)
        print("Division:", self.div)


c = CalculatorDetails(10, 45, 20, 47)

c.display()