# coding: utf-8

# PEP-8

"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен выводить
уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашем")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")

example1 = Stationery()
print(example1.title)
example1.title = "Канцелярка"
print(example1.title)
example1.draw()

example2 = Pen()
print(example2.title)
example2.title = "ручка"
print(example2.title)
example2.draw()

example3 = Pencil()
print(example3.title)
example3.title = "карандаш"
print(example3.title)
example3.draw()

example4 = Handle()
print(example4.title)
example4.title = "маркер"
print(example4.title)
example4.draw()