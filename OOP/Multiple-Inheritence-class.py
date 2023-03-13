# class X:
#     def display(self):
#         return "I am message from class X"
#
#
# class A:
#     b = 3
#     # def display(self):
#     #     return "I am message from class A"
#
#
# class B:
#     def display(self):
#         return "I am message from class B"
#
#
# class C(A, B):  # Multiple Inheritance
#     _a = 1  # Protected attribute
#     def display(self):
#         return "I am message from class C"
#
#     def access_a(self):
#         return self._a
#
#
# obj = C()
# print(obj.display())
# print(obj._a)
#
# """
# Inheritance
# Encapsulation
# Abstraction
#
# """


class Vehicle:
    def __init__(self):
        self.color = "red"
        self._mileage = 99
        self.__doors = 4

    def change_mileage(self, mileage):
        self._mileage = mileage


my_vehicle = Vehicle()
"""Cant access private members in this way"""
#print(my_vehicle.__doors)

"""This is called name mangling"""
print(my_vehicle._Vehicle__doors)
# print(my_vehicle._mileage)
# my_vehicle.change_mileage(25)
# print(my_vehicle._mileage)

"""This is also possible but not recommended"""
# my_vehicle._mileage = 10
# print(my_vehicle._mileage)
