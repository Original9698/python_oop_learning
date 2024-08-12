class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if not isinstance(value, (int, float)):
            return print(f"ErrorValue:{value}")
        elif value <= 0:
            return print(f"ErrorValue:{value}")
        self.__salary = value

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)
