class Employee:
    def __init__(self, name, __position, __hours_worked, __hourly_rate):
        self.name = name
        self.__position = __position
        self.__hours_worked = __hours_worked
        self.__hourly_rate = __hourly_rate

    def __calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    def _set_position(self,position):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return f'Name: {self.name}, Position: {self.__position}, Salary: {self.get_salary()}'
