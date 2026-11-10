class Shape:
    def display(self):
        print("Area of the shape")


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, width):
        return length * width


c = Circle()
c.display()
print("Circle Area:", c.area(5))

r = Rectangle()
r.display()
print("Rectangle Area:", r.area(4, 6))