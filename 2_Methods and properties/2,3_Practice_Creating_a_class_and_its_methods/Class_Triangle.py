class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def is_exists(self):
        if self.side_a < self.side_b + self.side_c and self.side_b < self.side_a + self.side_c and self.side_c < self.side_a + self.side_b:
            return True
        else:
            return False

    def is_equilateral(self):
        if self.is_exists():
            if self.side_a == self.side_b == self.side_c:
                return True
            else:
                return False
        else:
            return False

    def is_isosceles(self):
        if self.is_exists():
            if self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c:
                return True
            else:
                return False
        else:
            return False
