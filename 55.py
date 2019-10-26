# coding: utf-8

# PEP-8

"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os

num_list = input("Введите числа через пробел: ")
try:
    path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(path, "55_txt.txt"), "w") as file:  # открываем файл на запись
        print(num_list, file = file)  # записываем строку из чисел в файл
    with open("55_txt.txt") as file:  # открываем файл для чтения
        for line in file:
            line = line.split()
            arr_line = []
            for el in line:
                arr_line.append(int(el))  # заполняем список из чисел в файле
            print(f"Сумма элементов строки: {sum(arr_line)}")  # выводим сумму списка на экран
except IOError as e:
    print(e)
finally:
    print("работа с файлом завершена")