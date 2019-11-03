# coding: utf-8

# PEP-8
"""
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Date_Error(Exception):
    def __init__(self, message: str):
        self.message = message
        Exception.__init__(self)

    def __str__(self):
        return self.message

class Date:
    def __init__(self, date: str):
        if isinstance(date, str):
            self.date = date
        else:
            raise TypeError

    @classmethod
    def make_num(cls):
        pass

    @staticmethod
    def valid_num:
        pass


if __name__ == '__main__':
    pass