# coding: utf-8

# PEP-8

"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Пример списка: [{‘firm_1’: 5000, ‘firm_2’: 3000, ‘firm_3’: 1000}, {‘average_profit’: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Подсказка: использовать менеджер контекста.
"""
import json


try:
    res_list = []
    firm = {}
    with open("57_txt.txt") as file:
        for line in file:
            arr_line = line.replace("\n","").split("   ")  # удаляем перенос строки, создаем список
            if arr_line[2].isdigit() and arr_line[3].isdigit() and (int(arr_line[2]) - int(arr_line[3])) > 0:
                    firm[arr_line[0]] = int(arr_line[2]) - int(arr_line[3])  # вычисляем прибыль
        res_list.append(firm)
        ave_profit = sum(firm.values()) / len(firm)  # средняя прибыль фирм с положительной прибылью
        firm = {}
        firm['average_profit'] = ave_profit
        res_list.append(firm)
    with open("57_json.json", "w") as write_f:
        json.dump(res_list, write_f)  # записываем json объект в файл
except IOError as e:
    print(e)
finally:
    print("работа с файлом завершена")
