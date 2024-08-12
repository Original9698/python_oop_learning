class Person:
    def __init__(self, surname='Ivanov', name='Ivan', age=18):
        self.first_name = surname
        self.last_name = name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
# Ниже код для проверки методов класса Person
p1 = Person('Ash', 'Ketchum', 20)
assert isinstance(p1, Person)
assert p1.full_name() == 'Ketchum Ash'
assert p1.age == 20
assert p1.first_name == 'Ash'
assert p1.last_name == 'Ketchum'
assert p1.is_adult() is True

p2 = Person('Hermione', 'Granger', 16)
assert isinstance(p2, Person)
assert p2.age == 16
assert p2.first_name == 'Hermione'
assert p2.last_name == 'Granger'
assert p2.full_name() == 'Granger Hermione'
assert p2.is_adult() is False
print('Good')