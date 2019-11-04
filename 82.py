# coding: utf-8

# PEP-8
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""
class ZeroDevErr(Exception):
    def __init__(self, message: str):
        self.message = message
        Exception.__init__(self)
    def __str__(self):
        return self.message
class Dev:
    def __init__(self, val):
        self.val = int(val)

    def __truediv__(self, other):
        if other.val == 0:
            raise ZeroDevErr("На ноль делить нельзя")
        else:
            return self.val / other.val


if __name__ == '__main__':
    a = Dev(input("введите делимое: "))
    b = Dev(input("введите делитель: "))
    try:
        print(a / b)
    except ZeroDevErr as e:
        print(e)
