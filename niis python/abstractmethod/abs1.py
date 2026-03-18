from abc import ABC, abstractmethod

# Abstract class
class Perimeter(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

# Child class for Rectangle
class Rectangle(Perimeter):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Child class for Square
class Square(Perimeter):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

# Main program
r = Rectangle(10, 5)
s = Square(4)

print("Perimeter of Rectangle:", r.calculate_perimeter())
print("Perimeter of Square:", s.calculate_perimeter())