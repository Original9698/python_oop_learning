def double_it(func):
    def inner(*args, **kwargs):
        return 2*func(*args, **kwargs)
    return inner


@double_it
def multiply(num1, num2):
    return num1 * num2


res = multiply(9, 4)  # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)
