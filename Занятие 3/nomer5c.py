  # -*- coding: utf-8 -*-
def math():
    n = int(input('Введите число: '))
    sum = 0
    for i in range(n + 1):
        sum += i ** 3
    print("Ответ")
    return sum
print(math())