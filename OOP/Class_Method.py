# class Vehicle:
#     category = 'Car'
#
#     @classmethod
#     def printCategory(cls):
#         print(f'Vehicle category = {cls.category}')
#
#
# Vehicle.printCategory()
# my_vehicle = Vehicle()
# my_vehicle.printCategory()

# # Factory Method
#
# from datetime import date
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     def display(self):
#         print(f'{self.name} is {self.age} years old')
#
#
# Person1 = Person('Ram', 4)
# Person2 = Person('Ram', date.today().year - 2004)
# print(Person1.display())
# print(Person2.display())

#  Static Method

class Vehicle:

    @staticmethod
    def is_good_mileage(mileage):
        if mileage < 25:
            return "No"
        return "Yes"


print(Vehicle.is_good_mileage(25))
print(Vehicle.is_good_mileage(15))