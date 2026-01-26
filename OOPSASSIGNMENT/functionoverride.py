class Shape:
    def __init__(self):
        print("Parent class constructor called")

    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height



circ = Circle(7)
print(circ.get_area())

rect = Rectangle(2,4)
print(rect.get_area())

tri = Triangle(4,6)
print(tri.get_area())