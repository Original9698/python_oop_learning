def multiply(x: (int, float)) -> (int, float):
    def inner(y: (int, float)) -> (int, float):
        summer = x * y
        return summer

    return inner
