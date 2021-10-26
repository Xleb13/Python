# -*- coding: utf-8 -*-
def delet():
    s = input('Введите строку : ')
    s = s[:s.find('h')] + s[s.rfind('h') + 1:]
    print(s)
delet()