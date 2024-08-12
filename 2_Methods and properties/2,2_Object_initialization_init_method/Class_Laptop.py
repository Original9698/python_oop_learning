class Laptop:
    def __init__(self, brand='hp', model='1337', price='228'):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'


laptop1 = Laptop()
laptop2 = Laptop()
