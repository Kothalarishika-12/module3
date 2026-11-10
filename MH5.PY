class Addition:
    def add(self, a, b):
        print("Addition:", a + b)


class Multiplication:
    def multiply(self, a, b):
        print("Multiplication:", a * b)


class Calculator(Addition, Multiplication):
    pass


c = Calculator()
c.add(10, 5)
c.multiply(10, 5)

    