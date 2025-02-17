# Создайте класс Counter, экземпляры которого будут
# подсчитывать внутри себя значения.
# В классе Counter нужно определить:
# Метод start_from, который принимает один необязательный аргумент.
# Значение, с которого начинается подсчет, по умолчанию равно 0.
# Метод increment, который увеличивает счетчик на 1.
# Метод display, который печатает фразу
# "Текущее значение счетчика = <value>".
# Метод reset, который обнуляет накопившееся значение счетчика.

# Напишите определение класса Counter
class Counter:
    def start_from(self, ct=0):
        self.n = ct

    def increment(self):
        self.n += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.n}')

    def reset(self):
        self.n = 0


# Ниже код для проверки класса Counter

c1 = Counter()
c2 = Counter()

assert isinstance(c1, Counter)
assert isinstance(c2, Counter)
assert c1.__dict__ == {}
assert c2.__dict__ == {}

c1.start_from(45)
assert len(c1.__dict__) == 1
c1.increment()
c1.display()  # печатает 46
c1.increment()
c1.display()  # печатает 47

c2.start_from()
c2.display()  # печатает 0
c2.increment()
c2.display()  # печатает 1

c1.reset()  # обнулили с1, но с2 не должен меняться
c1.display()  # печатает 0

c2.display()  # по прежнему печатает 1
