import math

# Base class
class Polygon:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Rectangle
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Square
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Circle
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Trapezium
class Trapezium(Polygon):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


# Demonstration
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Square(4),
        Triangle(6, 8),
        Circle(7),
        Trapezium(10, 6, 5)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")


