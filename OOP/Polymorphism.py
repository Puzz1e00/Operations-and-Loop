#  This is function Overloading as both function have same name but it is not possible in Pycharm

# def addition(a, b):
#     return a + b
#
#
# def addition(a, b, c):
#     return a + b + c
#
#
# print(addition(1, 2))
# print(addition(1, 2, 3))

# Overloading is not possible in python

# Error Case

# class Shape:
#     def area(self, l):
#         return l * l
#
#     def area(self, l, b):
#         return l * b
#
#
# square = Shape()
# print(square.area(5))

#  Output of above will be error

#  Output of below will be not be an error

class Shape:
    def area(self, l, b=None):
        if b is not None:
            return l * b
        return l * l


square = Shape()
print(square.area(5))
print(square.area(2, 4))
