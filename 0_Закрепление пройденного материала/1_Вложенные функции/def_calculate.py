def calculate(x: float, y: float, operation: str = 'a'):
    def addition(w):
        if w == 'a':
            return print(x + y)

    def subtraction(w):
        if w == 's':
            return print(x - y)

    def division(w):
        if w == 'd':
            if y == 0:
                return print('На ноль делить нельзя!')
            else:
                return print(x / y)

    def multiplication(w):
        if w == 'm':
            return print(x * y)

    if operation not in ('a', 's', 'd', 'm'):
        return print('Ошибка. Данной операции не существует')
    addition(operation)
    subtraction(operation)
    division(operation)
    multiplication(operation)
calculate(1,2)