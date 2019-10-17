# coding: utf-8

# PEP-8

"""
3.Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_func(var1, var2, var3):
    """
    Функция принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов.
    :param var1: int
    :param var2: int
    :param var3: int
    :return: int
    """
    return var1 + var2 + var3 - min(var1, var2, var3)

print(my_func(3, 5, 7))  # 12
