# Создайте класс Lion. В нем должен быть метод roar,
# который печатает на экран "Rrrrrrr!!!"
class Lion:
    def roar(self):
        print('Rrrrrrr!!!')


# Ниже код для проверки класса Lion
s = Lion()
assert isinstance(s, Lion)
assert s.__dict__ == {}
s.roar()
