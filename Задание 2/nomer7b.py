# -*- coding: utf-8 -*-
def year():
    year = int(input('Введите число :'))
    if( (year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print('Да')
    else:
       print('Нет')
        
year()