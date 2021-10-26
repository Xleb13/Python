# -*- coding: utf-8 -*-
def poradok():
    A = int(input("Введите первое число: "))
    B = int(input("Введите второе число: "))
    for i in range(A,B-1,-1):
        if(i % 2 != 0):
            print(i)
    return 'Конец'
print(poradok())