# -*- coding: utf-8 -*-
def found():
    s = input('Введите строку : ')
    if (s.count("f") == 1):
        print(s.find("f"))
    if (s.count("f") >= 2):
        print('Первый индекс : ', s.find("f"))
        print('Последний индекс : ', s.rfind("f")) 
found()