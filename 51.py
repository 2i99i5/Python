# coding: utf-8

# PEP-8

"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

try:
    with open("51_txt.txt", "w") as file:
        while True:
            string = input("Введите строку: ")
            if string != "":
                file.write(string + "\n")  # добавляем перенос строки
            else:
                break
except IOError as e:
    print(e)
finally:
    print("работа с файлом завершена")