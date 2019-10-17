# coding: utf-8

# PEP-8

"""
2.Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
def output(name, surname, d_birth, city, email, phone):
    """
    Функция реализует вывод данных о пользователе одной строкой
    :param name: str
    :param surname: str
    :param d_birth: int
    :param city: str
    :param email: str
    :param phone: str
    :return:
    """
    print(f"{name} {surname} {d_birth} {city} {email} {phone}")

"""
output(
surname = input("Введите фамилию пользователя: "),
name = input("Введите имя пользователя: "),
d_birth = input("Введите год рождения пользователя: "),
city = input("Введите город проживания пользователя: "),
email = input("Введите email пользователя: "),
phone = input("Введите телефон пользователя: ")
)
"""

output(name = "Иван", surname = "Иванов", d_birth = 1900, city = "Moscow", email = "mail@mail.com", phone = "+79999999999")

