# coding: utf-8

# PEP-8

"""
Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar.
У каждого класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также несколько методов: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
"""
class Car:
    def __init__(self, speed = 0, color = None, name = None):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")

class TownCar(Car):
    is_police: bool = False
class SportCar(Car):
    is_police: bool = False
class WorkCar(Car):
    is_police: bool = False
class PoliceCar(Car):
    is_police: bool = True

Lada = PoliceCar(100, "бело-синяя", "полицейский")
Lada.go()
Lada.turn("нелево")
Lada.stop()
print(Lada.is_police)
Mercedes = SportCar(200, "красная", "блондинки")
print(Mercedes.is_police)