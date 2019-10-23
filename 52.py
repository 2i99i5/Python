# coding: utf-8

# PEP-8

"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("52_txt.txt", "r") as file:
        count_l = 0
        for line in file:
            count_l +=1
            line = line.replace("-", "")  # удаляем "-" в строке
            print(f"В {count_l} строке {len(line.split())} слов")  # выводим кол-во слов
        print(f"Количество строк: {count_l}")
except IOError as e:
    print(e)
finally:
    print("работа с файлом завершена")
