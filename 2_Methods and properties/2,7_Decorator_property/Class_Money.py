class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollar):
        if type(dollar) != int:
            return print("Error dollars")
        if dollar < 0 and dollar:
            return print("Error dollars")
        self.total_cents = dollar * 100 + self.total_cents % 100

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cent):
        if type(cent) != int:
            return print("Error cents")
        if not 0 <= cent < 100:
            return print("Error cents")
        self.total_cents = self.total_cents // 100 * 100 + cent

    def __str__(self):
        return f'Ваше состояние составляет {self.total_cents // 100} долларов {self.total_cents % 100} центов'


bill = Money(101, 99)
assert isinstance(bill, Money)

print(bill)  # Ваше состояние составляет 101 долларов 99 центов
print(bill.dollars, bill.cents)  # 101 99
bill.dollars = 666
print(bill)  # Ваше состояние составляет 666 долларов 99 центов
bill.cents = 12
print(bill)  # Ваше состояние составляет 666 долларов 12 центов
assert bill.total_cents == 66612

ken = Money(111, 90)
assert isinstance(ken, Money)
print(ken)
ken.dollars = 'hello'  # Error dollars
ken.dollars = 0
print(ken)
ken.cents = [1, 2, 3]  # Error cents
ken.cents = 100  # Error cents
ken.cents = 99
print(ken)
