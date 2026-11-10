class Animal:
    def eat(self):
        print("Animal is eating")


class Bird:
    def fly(self):
        print("Bird is flying")


class Parrot(Animal, Bird):
    pass


p = Parrot()
p.eat()
p.fly()