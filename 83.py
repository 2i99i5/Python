# coding: utf-8

# PEP-8
"""
Создайте собственный класс-исключение, который должен проверять
содержимое списка на отсутствие элементов типа строка и булево.
Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""
class MyException(Exception):
    def __init__(self, message: str):
        self.message = message
        Exception.__init__(self)
    def __str__(self):
        return self.message
class Check:
    def __init__(self, arr: list):
        self.arr = arr
        for el in self.arr:
            if isinstance(el, str) or isinstance(el, bool):
                raise MyException("В списке есть элемент строка или булевый")

    def __str__(self):
        return f"{self.arr}"


if __name__ == '__main__':
    try:
        array = Check([3, "4", True, 8])
        print(array)
    except MyException as e:
        print(e)
