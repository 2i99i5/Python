# coding: utf-8

# PEP-8

"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

try:
    path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(path, "53_txt.txt"), "r") as file:
        ave_sal = 0
        count = 0
        print(f"Сотрудники, оклад которых меньше 20тыс.:")
        for line in file:
            arr_line = line.split()
            if float(arr_line[1]) < 20000:
                print(arr_line[0])
            count += 1
            ave_sal += float(arr_line[1])
        print(f"\nСредняя зарплата всех сотрудников: {ave_sal / count}")
except IOError as e:
    print(e)
finally:
    print("работа с файлом завершена")
