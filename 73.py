# coding: utf-8

# PEP-8
"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""
class B_Cell_Error(Exception):
    def __init__(self, message: str):
        self.message = message
        Exception.__init__(self)

    def __str__(self):
        return self.message

class B_Cell:
    def __init__(self, cells: int):
        if isinstance(cells, int):
            if cells > 0:
                self.__cells = cells
            else:
                raise B_Cell_Error("Клетка не может быть меньше нуля")
        else:
            raise TypeError

    @property
    def cells(self):
        return self.__cells

    def __add__(self, other):
        if isinstance(other, B_Cell):
            return B_Cell(self.cells + other.cells)
        else:
            raise B_Cell_Error("Требуется ввести вторую Клетку")

    def __sub__(self, other):
        if isinstance(other, B_Cell):
            if self.cells - other.cells > 0:
                return B_Cell(self.cells - other.cells)
            else:
                raise B_Cell_Error("Клетка не может быть меньше или равна нулю")
        else:
            raise B_Cell_Error("Требуется ввести вторую Клетку")


    def __mul__(self, other):
        if isinstance(other, B_Cell):
            return B_Cell(self.cells * other.cells)
        else:
            raise B_Cell_Error("Требуется ввести вторую Клетку")

    def __truediv__(self, other):
        if isinstance(other, B_Cell):
            return B_Cell(int(self.cells / other.cells))
        else:
            raise B_Cell_Error("Требуется ввести вторую Клетку")

    def __str__(self):
        return f"{'*'}" * (self.cells)

    def make_order(self, column: int):
        if not self.cells % column:
            return f"{'*' * column}\n" * (self.cells // column)
        else:
            return f"{'*' * column}\n" * (self.cells // column) + f"{'*' * (self.cells % column)}\n"

if __name__ == '__main__':
    a = B_Cell(23)
    b = B_Cell(11)
    print(a.make_order(10))
    print(a + b)
    print(a - b)
    print(a / b)
    print((a * b).make_order(22))