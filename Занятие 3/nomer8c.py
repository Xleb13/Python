# -*- coding: utf-8 -*-
def les():
    n = int(input('Введите от 1 до 9 : '))
    if(1 <= n <= 9):
        for z in range(1, n + 1):
            for e in range(1, z + 1):
                print(e, sep='', end='')
            print()
    else: 
        return 'Ошибка ввода'
    return ''
print(les())