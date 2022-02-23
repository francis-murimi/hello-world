class Person:
    def __init__(self, name):
        self.name = name

mtu = Person("John Doe")
print(mtu.name)

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

car = Car('Toyota', '2008')
print(car.brand + " " + car.year)