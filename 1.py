# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


import re

class Date:
    def __init__(self, date) -> str:
        reg = r'[0-3][0-9]-[0-1][0-9]-\d{4}'
        self.date = ''.join(map(str, re.findall(reg, date)))

    @classmethod
    def data_to_num(cls, date_str):
        dd, mm, yyyy = date_str.split('-')
        return dd, mm, yyyy


    @staticmethod
    def validation(date):
        dd, mm, yyyy = Date.data_to_num(date)
        d = lambda d : 0<d<32
        if not d(int(dd)):
            dd = None
        m = lambda m: 0 < m < 13
        if not m(int(mm)):
            mm = None
        y = lambda y: 0 < y < 2022
        if not y(int(yyyy)):
            yyyy = None
        return dd, mm, yyyy

ms = "31-12-2021"
a = Date(ms)

print(a.date)
print(Date.data_to_num(a.date))
print(a.validation(a.date))
