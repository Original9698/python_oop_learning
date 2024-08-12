class Vector:
    def __init__(self,*args):
        self.values = []
        for i in args:
            if type(i) is int:
                self.values.append(i)
        self.values.sort()

    def __str__(self):
        if len(self.values) == 0:
            return 'Пустой вектор'
        else:
            return f'Вектор{tuple(self.values)}'

v5 = Vector(1, 2, True)
print(v5) # печатает "Вектор(1, 2, 3)"