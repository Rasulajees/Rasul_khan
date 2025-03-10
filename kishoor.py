class Vehicle:  # Parent class
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        return "Unknown fuel"

class Car(Vehicle):  # Child class
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Vehicle):  # Another child class
    def fuel_type(self):
        return "Electric"

# Testing the classes
car = Car("Toyota")
#electric_car = ElectricCar("Tesla")
print(car.brand, "uses", car.fuel_type())
#print(electric_car.brand, "uses", electric_car.fuel_type())

