
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)


c1 = Car("Toyota", "Innova")
c2 = Car("Hyundai", "Creta")
c3 = Car("Honda", "City")

c1.display()
c2.display()
c3.display()
