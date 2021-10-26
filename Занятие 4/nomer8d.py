# -*- coding: utf-8 -*-
def miror():
    s = input('Введите строку : ')
    x = s.find('h')
    y = s.rfind('h')
    print(s[:x + 1] + s[x + 1:y][::-1] + s[y:])
miror()
