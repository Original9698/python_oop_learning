class PizzaMaker:
    def __make_pepperoni(self):
        print(1)

    def _make_barbecue(self):
        print(2)
maker = PizzaMaker()
print(dir(maker))
print(maker._PizzaMaker__make_pepperoni())
print(maker._make_barbecue())
