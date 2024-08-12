class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            v = []
            for i in self.values:
                v.append(i + other)
            return Vector(*v)
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                v = []
                for i in range(len(self.values)):
                    v.append(other.values[i] + self.values[i])
                return Vector(*v)
            else:
                return print('Сложение векторов разной длины недопустимо')
        if not isinstance(other, (int, Vector)):
            return print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            v = []
            for i in self.values:
                v.append(i * other)
            return Vector(*v)
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                v = []
                for i in range(len(self.values)):
                    v.append(other.values[i] * self.values[i])
                return Vector(*v)
            else:
                return print('Умножение векторов разной длины недопустимо')
        if not isinstance(other, (int, Vector)):
            return print(f'Вектор нельзя умножить с {other}')


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"
