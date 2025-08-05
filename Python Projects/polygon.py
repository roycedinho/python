import math

# Base class
class Polygon:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


# Square class
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)


# Driver Code
if __name__ == "__main__":
    # Rectangle
    rect = Rectangle(10, 5)
    print("Rectangle Area:", rect.area())

    # Square
    sq = Square(6)
    print("Square Area:", sq.area())

    # Triangle
    tri = Triangle(8, 4)
    print("Triangle Area:", tri.area())

    # Circle
    circ = Circle(7)
    print("Circle Area:", circ.area())
