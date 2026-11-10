class Device:
    def power_on(self):
        print("Device is switched on")
class Computer(Device):
    def run_program(self):
        print("Computer is running a program")
class Phone(Device):
    def make_call(self):
        print("Phone is making a call")
class SmartPhone(Computer, Phone):
    def take_photo(self):
        print("Smartphone is taking a photo")
s = SmartPhone()
s.power_on()
s.run_program()
s.make_call()
s.take_photo()