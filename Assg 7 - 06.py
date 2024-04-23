class Car:
    def method(self):
        print("Super Class")

class Sedan(Car):
    def method(self):
        print("Subclass")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()