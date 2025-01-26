from math import pi


class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        super().__init__()
        self.length = float(length)
        self.width = float(width)

    def area(self):
        rectangle_area = self.length * self.width
        return int(rectangle_area)


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
