# coding: utf-8

# PEP-8

"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"profit": profit, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_full_profit). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, income = {'profit': 0, "bonus": 0}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income: dict = income

class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")
    def get_full_profit(self):
        print(f"Доход: {sum(self._income.values())}")

builder = Position("John", "Doe", "carpenter", {"profit": 1000, "bonus": 100})  # создаем экземпляр
builder.get_full_name()
builder.get_full_profit()
dancer = Position("Ivan", "Ivanov", "dancer", {"profit": 2000, "bonus": 500})  # создаем экземпляр
dancer.get_full_name()
dancer.get_full_profit()
print(dancer._income)
print(builder.position)