# coding: utf-8

# PEP-8
"""
Реализовать программу работы с клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий исходному количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса и количество клеток в ряду.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество клеток между \n равно
переданному аргументу, а количество рядов определяется, исходя из исходного количества клеток.
Например, исходное количество клеток равняется 7, количество клеток в ряду — 5.
Тогда метод make_cell() вернет строку: *****\n*****\n*****\n*****\n*****\n*****\n*****.
При создании экземпляра клетки должна происходить перезапись параметра,
который хранит исходное количество клеток.
"""

class Cell:
    def __init__(self, num):
        self.num = num
        self.string = ""

    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __truediv__(self, other):
        pass
    def make_cell(self):
        return self.string


