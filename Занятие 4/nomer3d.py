# -*- coding: utf-8 -*-
def perevorot():
    s = input('Введите строку : ')
    l = len(s) // 2 + len(s) % 2
    a = s[0:l]
    b = s[l:]
    print(b + a)
perevorot()