class Vehicle:
    def __init__(self, doors ,color):
        self.doors = doors
        self.color = color


class Bike(Vehicle): # this is single inheritance
    def __init__(self,doors ,color, wheels):  # this is called method overriding
        self.wheels = wheels
        super().__init__(doors,color) #calling mathiko init
        """If we don't add init method in the child class then the init from parent class is called"""


class Car(Vehicle):
    def __init__(self,doors, color, mileage ):
        self.mileage = mileage
        super().__init__(doors, color)


honda = Bike(0, 'red', 2)
rover = Car(4, 'blue', 25)

print(honda.color)
print(rover.doors)

