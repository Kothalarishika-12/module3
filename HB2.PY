class Animal:
    def eat(self):
        print("Animal is eating")


class Mammal(Animal):
    def walk(self):
        print("Mammal can walk")


class Bird(Animal):
    def fly(self):
        print("Bird can fly")


class Bat(Mammal, Bird):
    def sound(self):
        print("Bat makes sounds")


b = Bat()
b.eat()
b.walk()
b.fly()
b.sound()