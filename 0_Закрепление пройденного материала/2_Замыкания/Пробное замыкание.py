def main_func():
    local1 = 0

    def inner():
        nonlocal local1
        local1+=1
        return local1

    return inner


a = main_func()
print(a())
print(a())
print(a())
print(a())
