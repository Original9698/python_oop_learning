def repeater(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return inner


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 7)  # после этого на отдельных строка дважды распечатается значение 14
multiply(5, 3)  # после этого на отдельных строка дважды распечатается значение 15
