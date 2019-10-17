# coding: utf-8

# PEP-8

"""
1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def devision_func(var_1, var_2):
    """
    Функция выполняет деление двух чисел, выводит результат деления.
    :param var_1: int
    :param var_2: int
    :return:
    """
    try:
        var_1 = int(var_1)
        var_2 = int(var_2)
        res = var_1 / var_2
    except ValueError as e:
        res = "Необходимо было ввести число."
    except ZeroDivisionError as e:
        res = "Невозможно выполнить деление на ноль."
    return res

var_1 = input("Введите делимое: ")
var_2 = input("Введите делитель: ")
print(devision_func(var_1, var_2))
