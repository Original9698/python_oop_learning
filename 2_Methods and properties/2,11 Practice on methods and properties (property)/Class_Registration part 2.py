from string import ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit(password):
        digits = '0123456789'
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        upper = 0
        lower = 0
        for i in password:
            if upper >= 1:
                upper = True
                break
            if i.title():
                upper += 1
        for i in password:
            if lower >= 1:
                lower = True
                break
            if i.islower():
                lower += 1
        if lower and upper:
            return True
        else:
            return False

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            if i not in ascii_letters and i not in '0123456789':
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        with open('easy_passwords.txt', 'r') as passwords:
            for i in passwords:
                if password in i:
                    return True
            return False

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if not isinstance(login, str):
            raise TypeError('Логин должен быть строкой')
        if '@' not in login:
            raise ValueError('Логин не является почтой')
        if '.' not in login[login.index('@') + 1:]:
            raise ValueError('Логин не является почтой')
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError('Пароль должен быть строкой')
        if 4 < len(password) and len(password) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')

        self.__password = password


try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')
