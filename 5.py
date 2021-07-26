# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
# за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).


from abc import ABC, abstractmethod


class Warehouse(ABC):
    add_store = {}

    @abstractmethod
    def number_ind(self):
        pass

    def acceptance_to_the_warehouse(self, col):
        try:
            col = int(col)
        except ValueError:
            print("col - it is int")
        else:
            str_name = str(self.__class__)
            col_symb = 3    #количество символов __.
            str_name = str_name[str_name.find('__.')+col_symb:str_name.find('\'>')]
            Warehouse.add_store.update({str_name : col})

    def department(self, n_d):
        self.name_dep = n_d


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
p.acceptance_to_the_warehouse(4)
p.department("big_boss")

print(p.add_store.items(), p.name_dep)
