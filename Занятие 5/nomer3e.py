# -*- coding: utf-8 -*-
n = int(input("Введите n : "))
i = 2
e = 1
while i <= n:
    i *= 2
    e += 1
print("Показатель степени : ", e - 1, "\nСтепень : ", i //2)
