# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} go"

    def stop(self):
        return f"{self.name} stop"

    def turn(self, direction):
        return f"turn {direction}"

    def show_speed(self):
        return f"speed: {self.speed}"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"speeding {self.speed} > 60"
        else:
            return f"speed {self.speed}"

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"speeding {self.speed} > 40"
        else:
            return f"speed {self.speed}"


class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

my_tc = TownCar(50, "green", "Car_for_Town")
my_wc = WorkCar(80, "gray", "Car_for_work")
my_sc = SportCar(230, "yellow", "Car_for_fanny")
my_pc = PoliceCar(150, "wight", "Car_for_Police")

print(f"{my_pc.name} {my_pc.turn('left')}")
print(f"{my_wc.name} {my_wc.show_speed()}")
print(f"{my_sc.name} {my_sc.color}")
print(f"{my_tc.name} {my_tc.show_speed()}")