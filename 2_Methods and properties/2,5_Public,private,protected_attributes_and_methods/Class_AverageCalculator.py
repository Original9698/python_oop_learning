class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def public_calcylate(self):
        return self.__calculate_average()

    def __calculate_average(self):
        total = sum(self.numbers)
        return total / len(self.numbers)


average_calculator = AverageCalculator([1, 2, 3])
print(average_calculator.public_calcylate())
