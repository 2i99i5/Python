# coding: utf-8

# PEP-8

"""
6.Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count
from itertools import cycle

def gen(num):
    list1 = []
    for el in count(num):
        if el > 15:  # условие выхода из бесконечного цикла
             break
        else:
            list1.append(el)
    return(list1)

print(gen(7))  # бесконечный итератор, генерирующий целые числа, начиная с указанного,

progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)
i = 0
while True:
    print(next(iter))
    if i > 15:  # условие выхода из бесконечного цикла
        break
    i += 1
