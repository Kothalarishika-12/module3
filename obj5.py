
class Mobile:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def display(self):
        print("Mobile Brand:", self.brand)
        print("Mobile Color:", self.color)
        print("Mobile Price:", self.price)


m1 = Mobile("Samsung", "Black", 20000)
m2 = Mobile("Apple", "White", 50000)
m3 = Mobile("Redmi", "Blue", 15000)

m1.display()
m2.display()
m3.display()
