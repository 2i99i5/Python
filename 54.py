# coding: utf-8

# PEP-8

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os

dict_ru = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}  # словарь с ru  числительными
try:
    path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(path, "54_en.txt"), "r") as file_en:
        file_ru = open("54_ru.txt", "w")
        for line in file_en:
            arr_line = line.replace("\n","").split(" — ")  # удаляем перенос строки, создаем список
            arr_line[0] = dict_ru.get(arr_line[1], arr_line[0])  # переводим en  на ru,  если в словаре нет, оставляем как есть
            print(" - ".join(arr_line), file = file_ru)  # записываем строку в новый файл
        file_ru.close()
except IOError as e:
    print(e)
finally:
    print("работа с файлами завершена")
