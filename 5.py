# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
#     определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#     создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#     в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#     создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):

    def draw(self):
        return f"Запуск отрисовки ручкой"

class Pencil(Stationery):

    def draw(self):
        return f"Запуск отрисовки карандашом"

class Handle(Stationery):
    def draw(self):
        return f"Запуск отрисовки маркером"

my_pen = Pen("Ручка")
my_pencil = Pencil("Карандаш")
my_handle = Handle("Маркер")

print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())

