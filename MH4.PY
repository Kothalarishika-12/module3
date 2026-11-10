class Camera:
    def take_photo(self):
        print("Taking a photo")


class Phone:
    def make_call(self):
        print("Making a phone call")


class SmartPhone(Camera, Phone):
    pass


s = SmartPhone()
s.take_photo()
s.make_call()