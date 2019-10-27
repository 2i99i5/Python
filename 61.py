# coding: utf-8

# PEP-8

"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Время перехода между режимами должно составлять 7 и 2 секунды. Проверить работу примера,
создав экземпляр и вызвав описанный метод.
"""
import itertools
import time

class TrafficLight:  # Класс светофор
    __color = None  # атрибут цвет

    def running(self):  # метод запуск
        colors = ["red", "green"]
        for el in itertools.cycle(colors):
            __color = el
            print(__color)
            time.sleep(7)
            __color = "yellow"
            print(__color)
            time.sleep(2)


street_light = TrafficLight()  # создаем экземпляр
street_light.running()  # вызываем метод запуск
