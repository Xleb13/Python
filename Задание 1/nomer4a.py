# -*- coding: utf-8 -*-

# Четвёртое задание
def lengthOfLace():
    print("Введите входные данные (4 числа)")
    a = int(input("Расстояние между рядами - "))
    b = int(input("Расстояние между отверстиями в ряду - "))
    l = int(input("Длина свободного конца шнурка - "))
    N = int(input("Кол-во отверстий в ряду - "))
    print("Ответ:")
    return (2 * N - 1) * a + 2 * l + 2 * (N - 1) * b

print("Четвёртое задание: ")
print(lengthOfLace())
print("\n")