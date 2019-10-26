# coding: utf-8

# PEP-8

"""
Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и
лабораторных занятий по этому предмету и их количество. Важно,
чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""

import os

try:
    path = os.path.dirname(os.path.abspath(__file__))
    subject = dict()
    with open(os.path.join(path, "56_txt.txt")) as file:
        for line in file:
            arr_line = line.replace("\n","").split(":")  # удаляем перенос строки, создаем список
            arr_line[1] = arr_line[1].split(",")
            quantity = 0
            for ed_type in arr_line[1]:
                ed_type = ed_type.split("-")
                if ed_type[1].isdigit():
                    quantity += int(ed_type[1])  # суммируем кол-во уроков
            subject[arr_line[0]] = quantity  # заполняем словарь
        print(subject)
except IOError as e:
    print(e)
finally:
    print("работа с файлом завершена")
