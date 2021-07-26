# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
from abc import ABC, abstractmethod


class Warehouse(ABC):
    @abstractmethod
    def number_ind(self):
        pass

class OfficeEquipment(ABC):

    @abstractmethod
    def work_paper(self):
        pass

class Printer (Warehouse, OfficeEquipment):
    def __init__(self, n):
        self.num_ind = n

    def number_ind(self):
        return self.num_ind

    def work_paper(self):
        return 'i wont to print'


class Scaner(Warehouse, OfficeEquipment):
    def __init__(self, n):
        self.num_ind = n

    def number_ind(self):
        return self.num_ind

    def work_paper(self):
        return 'i wont to scan'

class Xerox(Warehouse, OfficeEquipment):
    def __init__(self, n):
        self.num_ind = n

    def number_ind(self):
        return self.num_ind

    def work_paper(self):
        return 'i wont to Xerox'

p = Printer(1)
print(p.work_paper())

