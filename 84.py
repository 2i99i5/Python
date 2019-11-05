# coding: utf-8

# PEP-8
"""
Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет
базовым для классов-наследников. Эти классы — конкретные типы
оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Stock:
    def __init__(self):
        self.equip = []


class Equipment:
    def __init__(self, inventory_no, manufacturer, model, part_no, serial_no, price, paper="A4"):
        self.inventory_no = inventory_no
        self.manufacturer = manufacturer
        self.model = model
        self.part_no = part_no
        self.serial_no = serial_no
        self.price = price
        self.paper = paper


class Printer(Equipment):
    def __init__(self, inventory_no, manufacturer, model, part_no, serial_no, price, duplex=True):
        self.print_format = print_format
        self.duplex = duplex
        super(Printer, self).__init__(inventory_no, manufacturer, model, part_no, serial_no, price, paper)


class Scanner(Equipment):
    def __init__(self, inventory_no, manufacturer, model, part_no, serial_no, price, duplex=False, adf=False):
        self.scan_format = scan_format
        self.duplex = duplex
        self.adf = adf
        super(Scanner, self).__init__(inventory_no, manufacturer, model, part_no, serial_no, price, paper)


class Copier(Equipment):
    def __init__(self, inventory_no, manufacturer, model, part_no, serial_no, price, duplex=False, adf=True):
        self.copy_format = copy_format
        self.duplex = duplex
        self.adf = adf
        super(Copier, self).__init__(inventory_no, manufacturer, model, part_no, serial_no, price, paper)


if __name__ == '__main__':
    pass
