class Cell:
    def __init__(self, n) -> int:
        self.number = n

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __floordiv__(self, other):
        return self.number // other.number

    def __truediv__(self, other):
        return self.number / other.number

    def __mod__(self, other):
        return self.number % other.number

    def make_order(self, row_num):
        whol_str = self.number // row_num
        fractional_str = self.number % row_num
        return  f'{"*" * row_num}\n' * whol_str + f"{fractional_str*'*'}"

a = Cell(8)
b = Cell(13)

print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(b//a)

print(b.make_order(5))
