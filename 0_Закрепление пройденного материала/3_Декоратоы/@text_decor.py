def text_decor(text):
    def inner(*args, **kwargs):
        print('Hello')
        text(*args, **kwargs)
        print('Goodbye!')

    return inner


@text_decor
def multiply(num1, num2):
    print(num1 * num2)


multiply(3, 5)
