# coding: utf-8

# PEP-8

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

args = argv
try:
    prod_per_hour = int(argv[1])
    rate = float(argv[2])
    bounty = float(argv[3])
except Exception as e:  # обработка ошибок
    print(e)
    exit()

print("Выработка в часах: ", prod_per_hour)
print("Ставка в час: ", rate)
print("Премия: ", bounty)
print(f"Заработная плата сотрудника: {prod_per_hour} * {rate} + {bounty} = {prod_per_hour * rate + bounty}")