def is_include_all_register(password):
    upper = 0
    lower = 0
    for i in password:
        if upper >= 1:
            upper = True
            break
        if i.title():
            upper += 1
    for i in password:
        if lower >= 1:
            lower = True
            break
        if i.islower():
            lower += 1
    if lower and upper:
        return True
    else:
        return False

is_include_all_register('Title')