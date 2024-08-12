class WeatherStation:
    __share_ = {
        "temperature": 0,
        "humidity": 0,
        "pressure": 0
    }

    def __init__(self):
        self.__dict__ = WeatherStation.__share_

    def update_data(self, temperature=0, humidity=0, pressure=0):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def get_current_data(self):
        return (self.temperature, self.humidity, self.pressure)
