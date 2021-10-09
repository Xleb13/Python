# -*- coding: utf-8 -*-
def ravenstvo():
    print("Введите 3 числа : ")
    a = int(input())
    b = int(input())
    c = int(input())
    if(a == b == c):
        print("Ответ:", 3)
    elif((a == b) or (c == b) or (a == c)):
        print("Ответ:", 2)
    else:
        print("Ответ:", 0)       
ravenstvo()