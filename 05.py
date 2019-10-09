# coding: utf-8

# PEP-8

a = input("Результат пробежки в первый день: ")
b = input("Требуемый общий результат: ")
total = 0  # общая дистанция
if a.isdigit() and b.isdigit():  # проверка ввода
    count = 1  # кол-во дней
    a = int(a)
    b = int(b)
    total = a
    while total < b:
        a = a * 1.1
        total = total + a
        count += 1
    print(f"На {count} день спортсмен достиг результата {b}")
else:
    print("Необходимо ввести числа, программа завершена")
