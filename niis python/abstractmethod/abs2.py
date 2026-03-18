from abc import ABC, abstractmethod

# Abstract class
class Area(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

# Child class for Rectangle
class Rectangle(Area):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Child class for Circle
class Circle(Area):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Main program
r = Rectangle(10, 5)
c = Circle(7)

print("Area of Rectangle:", r.calculate_area())
print("Area of Circle:", c.calculate_area())