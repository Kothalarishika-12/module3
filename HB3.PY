class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


e = ElectricCar()
e.start()
e.drive()
e.charge()