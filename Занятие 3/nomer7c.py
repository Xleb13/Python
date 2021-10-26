# -*- coding: utf-8 -*-
n = int(input('Введите число: '))
def fctrl(n):
    x=n
    s=0
    fct=1
    for i in range(1, x + 1):
        fct = fct * i
        s = s + fct
    else:
        print('Сумма: ')
        return s
print(fctrl(n))