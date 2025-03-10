#vehicals:
"""class vehicle:
    def __init__(self,Brand):
        self.brand= Brand

    def fuel_type(self):
        return"Unknown fuel type"
    
    
class car(vehicle):
    def fuel_type(self):
        return "Petrol or Diesel type"
    
    def electric_type(self):
        return "Electric vehicle"
    
#Testing the classes
Car=car("BMW")
#electric_car=car("Tesla")
print(Car.brand,"uses",car.fuel_type())
#print(electric_car.brand,"uses",electric_car.fuel_type())
"""

class animal:
    def __init__(self,name):
        self.name=name

    def animal_type(self):
        return "Some sounds"
    
class dog(animal):
    def animal_type(self):
        return "Barks"
    
class cat(animal):
    def animal_type(self):
        return "Meows"
    
#Testing the classes
dog=dog("Dog")
cat=cat("Cat")
print(dog.name,"makes",dog.animal_type())
print(cat.name,"makes",cat.animal_type())