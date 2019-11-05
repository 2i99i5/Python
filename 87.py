# coding: utf-8

# PEP-8
"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, val: complex):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __mul__(self, other):
        return self.val * other.val

    def __str__(self):
        return f"{self.val}"


if __name__ == '__main__':
    x = Complex(complex(1, 2))
    y = Complex(complex(3, 4))
    assert x + y == (4+6j)
    assert x * y == (-5+10j)
