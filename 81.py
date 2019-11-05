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
from datetime import datetime

class Date:
    def __init__(self, date):
        if not Date.validate(date):
            self.date = date

    @staticmethod
    def validate(date_text):
        try:
            datetime.strptime(date_text, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")

    @classmethod
    def make_num(cls, date):
        numlist = []
        for num in date.split("-"):
            numlist.append(int(num))
        return numlist




if __name__ == '__main__':
    d = Date("04-12-2019")
    print(d.make_num("05-12-2019"))
    print(Date.validate("35-11-2019"))