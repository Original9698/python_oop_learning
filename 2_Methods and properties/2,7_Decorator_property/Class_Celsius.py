class Celsius:
    def __init__(self, grad):
        self.__temp = grad

    def to_fahrenheit(self):
        return (self.__temp * 9 / 5) + 32
    @property
    def temperature(self):
        return self.__temp
    @temperature.setter
    def temperature(self,new_temp):
        if self.__temp == -273.15:
            raise ValueError('Не можно так плохо')
        else:
            self.__temp = new_temp

celsius = Celsius(25)
assert celsius.temperature == 25
assert celsius.to_fahrenheit() == 77.0

celsius.temperature = 30
assert celsius.temperature == 30
assert celsius.to_fahrenheit() == 86.0

print('Good')