class Rectangle:
    def __init__(self, a: int, b: int):
        self.width = a
        self.height = b

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height
