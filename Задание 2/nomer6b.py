# -*- coding: utf-8 -*-
def chahmati():
    x1 = int(input("Номер столбца 1ой клетки: "))
    y1 = int(input("Номер строки 1ой клетки: "))
    x2 = int(input("Номер столбца 2ой клетки: "))
    y2 = int(input("Номер строки 2ой клетки: "))
    if x1 % 2 == x2 % 2:
        if y1 % 2 == y2 % 2:
            return "Да"
        else:
            return "Нет"
    else:
        if y1 % 2 != y2 % 2:
            return "Да"
        else:
            return "Нет"
print(chahmati())