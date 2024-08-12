class Zebra:
    def __init__(self):
        self.color1 = 'Полоска белая'
        self.color2 = 'Полоска черная'

    def run_away(self):
        print('Oh, Sugar Honey Ice Tea')

    def which_stripe(self):
        print(self.color1)
        self.color1, self.color2 = self.color2, self.color1
