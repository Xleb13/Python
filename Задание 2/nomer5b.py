# -*- coding: utf-8 -*-
def small():
    a = int(input('Введите первое число : '))
    b = int(input('Введите второе число : '))
    c = int(input('Введите третье число : '))
    print("Минимальное число ")
    return min(a,b,c)
print(small())
