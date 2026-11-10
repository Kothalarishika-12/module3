class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)


class AdvancedCalculator(Calculator):
    def multiply(self, a, b):
        print("Multiplication:", a * b)


class ScientificCalculator(AdvancedCalculator):
    def square(self, a):
        print("Square:", a * a)


s = ScientificCalculator()
s.add(10, 5)
s.multiply(10, 5)
s.square(5)