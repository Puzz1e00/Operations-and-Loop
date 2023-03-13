class Vehicle:
    category = ' car '

    def __init__(self, color, doors):
        self.color = color
        self.doors = doors

    def description(self):
        return f"This vehicle's color is {self.color} and it has {self.doors} doors."

    def make_it_blue(self):
        self.color = 'blue'


rover = Vehicle(' red ', ' 4 ')
print(f"Vehicle color: {rover.color}")
print(f"Vehicle category: {rover.category}")
print(f"Number of doors: {rover.doors}")
print(f"Category: {rover.__class__.category}")
print(rover.description())
rover.make_it_blue()
print(rover.color)
audi = Vehicle('green', 2)
print(f"Vehicle color: {audi.color}")
print(f"Vehicle category: {audi.category}")
print(f"Number of doors: {audi.doors}")
print(f"Category: {audi.__class__.category}")
print(audi.description())


# class Stationary:
#     category = "Pen"
#
#     def __init__(self, color, type):
#         self.color = color
#         self.type = type
#
#     def description(self):
#         f"This is a {self.color}{self.type}"
#
#     def make_it_black(self):
#         self.color = 'black'
#
#
# stationary = Stationary('blue', 'Ink pen')
# print(f"Pen color: {stationary.color}")
# print(f"Pen category: {stationary.category}")
# print(f"Pen type: {stationary.type}")
# print(f"Category: {stationary.__class__.category}")
# print(stationary.description())
# stationary.make_it_black()
# print(stationary.color)



