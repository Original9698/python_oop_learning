class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, x):
        self.__balance += x

    def is_money_enough(self, x):
        return x <= self.__balance

    def payment(self,pay):
        if self.is_money_enough(pay):
            self.__balance-=pay
        else:
            print('Не хватает средств на балансе. Пополните счет')


    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, x):
        self.__balance = x

    def is_money_enough(self, x):
        return x <= self.__balance

    def payment(self,pay):
        if self.is_money_enough(pay):
            self.__balance-=pay
        else:
            print('Не хватает средств на балансе. Пополните счет')
