class Circle:

    def __init__(self, radius):
        self.radius = radius

    #  def total_radius(self, obj):
        #  return self.radius + obj.radius

    def __add__(self, obj): # This is magic method/ dunder method
        return self.radius + obj.radius

    def __gt__(self, obj): # Magic Method to see greater
        return self.radius > obj.radius

    def __str__(self):
        return f'This is circle with radius {self.radius}'


c1 = Circle(2)
c2 = Circle(3)
#  result = c1.__add__(c2)
#  result = c1 + c2 this works due to magic method __add__
result = c1 > c2 # This works due to magic method __gt__
print(result)
print(c1)