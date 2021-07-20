class Cell:
    def __init__(self, n) -> int:
        self.number = n

    def __add__(self, other):
        return self.number + other

    def __sub__(self, other):
        return self.number - other

    def __mul__(self, other):
        return self.number * other

    def __floordiv__(self, other):
        return self.number // other

    def __truediv__(self, other):
        return self.number / other
