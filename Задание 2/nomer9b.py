# -*- coding: utf-8 -*-
def chokolat():
    print('Введите размер прямоугольнка , разделенного на n*m долек :')
    n = int(input())
    m = int(input())
    k = int(input('Введите часть долек , которая нужна : '))
    if(n * m > k and (k % m == 0 or k % n == 0)):
        print("Ответ : Да")
    else:
        print("Ответ : Нет")

chokolat()