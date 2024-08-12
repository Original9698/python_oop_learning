class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.__area = None

    @property
    def area(self):
        if self.__area == None:
            self.__area = self.height * self.width
        return self.__area


r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976
print('Good')
