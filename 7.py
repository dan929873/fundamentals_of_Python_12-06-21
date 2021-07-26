# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_number:

    def __init__(self, num):
        self.number = num

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number

a = Complex_number(7.8)
b = Complex_number(3.3)
print(a+b)
print(a*b)
