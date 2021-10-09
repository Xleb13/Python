# -*- coding: utf-8 -*-
n = int(input('Введите число миннут (n): '))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours,':', minutes)
