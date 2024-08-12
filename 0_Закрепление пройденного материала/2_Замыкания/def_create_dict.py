def create_dict():
    key =1
    dict = {}
    def inner(value):
        nonlocal key,dict
        dict.setdefault(key,value)
        key+=1
        return dict
    return inner