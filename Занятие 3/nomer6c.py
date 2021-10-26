# -*- coding: utf-8 -*-
def fctrl():
    n = int(input('Введите число: '))
    x = 1
    for z in range(1, n + 1):
        x *= z
    print('Ответ: ')
    return x

print(fctrl())