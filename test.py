class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __radd__(self, other):
        if isinstance(other, Number):
            return Vector(self.x + other.value, self.y + other.value)

    def __str__(self):
        return f"Vector({self.x},{self.y})"


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Vector):
            return Number(other.x + other.y + self.value)

    def __str__(self):
        return f"Number({self.value})"


v = Vector(2, 3)
num = Number(5)
print(num + v)