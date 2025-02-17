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
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if value > self.__balance:
            print("Не хватает средств на балансе. Пополните счет")
            return False
        else:
            self.balance -= value
            return True


class Cart:
    def __init__(self, User):
        self.user = User
        self.goods = {}
        self.__total = 0

    def add(self, Product, number=1):
        self.goods[Product] = self.goods.get(Product, 0) + number
        self.__total += number * Product.price

    def remove(self, Product, number=1):
        if number >= self.goods[Product]:
            number = self.goods[Product]
            self.goods[Product] = self.goods.get(Product, 0) - number
            self.__total -= number * Product.price

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print(f'---Your check---')
        for k, v in sorted(self.goods.items(), key=lambda x: x[0].name):
            if v > 0:
                print(k.name, k.price, v, k.price * v)
            else:
                pass
        print(f'---Total: {self.__total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 2 40
# ---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# ---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
cart_billy.order()
# ''' Печатает текст ниже
# Не хватает средств на балансе. Пополните счет
# Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20