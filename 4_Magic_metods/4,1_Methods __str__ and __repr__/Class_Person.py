class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender

    def __str__(self):
        if self.__gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        if self.__gender == 'female':
            return f'Гражданка {self.surname} {self.name}'

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value == 'male' or value == 'female':
            self.__gender = value
        else:
            self.__gender = 'male'
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')

