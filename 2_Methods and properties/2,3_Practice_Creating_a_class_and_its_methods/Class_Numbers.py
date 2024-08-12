class Numbers:
    def __init__(self, *args):
        self.nums = list(args)

    def add_number(self, num):
        self.nums.append(num)

    def get_positive(self):
        self.positive = [i for i in self.nums if i > 0]
        return self.positive

    def get_negative(self):
        self.negative=[i for i in self.nums if i < 0]
        return self.negative
    def get_zeroes(self):
        self.zero = [i for i in self.nums if i == 0]
        return self.zero

nums = Numbers(1, 2, -4, -5, 3)

print(nums.get_positive())
print(nums.get_negative())
print(nums.get_zeroes())