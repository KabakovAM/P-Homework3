# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

import random

def creat_rand_list():
    n = int(input('Введите размер списка: '))
    while n <= 0:
        print('Введён неверный размер списка')
        n = int(input('Введите размер списка: '))
    lis = []
    for i in range(n):
        lis.append(random.randint(1, 10))
    return lis

def sum_even_el(lis):
    sum = 0
    for i in range(0, len(lis), 2):
        sum += lis[i]
    print(lis)
    print(sum)

sum_even_el(creat_rand_list())
