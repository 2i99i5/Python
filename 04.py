# coding: utf-8

# PEP-8

rev = input("Введите сумму выручки: ")
costs = input("Введите сумму издержек: ")

if rev.isdigit() and costs.isdigit():  # проверка ввода
    rev = int(rev)
    costs = int(costs)
    if rev > costs:
        print(f"Фирма окончила период с прибылью")
        print(f"Рентабельность фирмы составляет: {(rev - costs) / rev * 100}%")
        num_emp = input("Введите количество сотрудников: ")
        if num_emp.isdigit():  # проверка ввода
            num_emp = int(num_emp)
            print(f"Прибыль в расчете на одного сотрудника: {(rev - costs) / num_emp}")
        else:
            print("Необходимо ввести целое положительное число, программа завершена")
    elif rev == costs:
        print(f"Фирма достигла точки безубыточности")
    else:
        print(f"Фирма окончила период с убытком")
else:
    print("Необходимо ввести целое положительное число, программа завершена")
