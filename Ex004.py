# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

import random

def creat_rand_list():
    n = int(input('Введите размер списка: '))
    while n <= 0:
        print('Введён неверный размер списка')
        n = int(input('Введите размер списка: '))
    lis = []
    for i in range(n):
        lis.append(round(random.uniform(1, 10), 2))
    print(lis)
    return (lis)

def max_min_tails(lis):
    for i in range(len(lis)):
        lis[i] = round(lis[i]-lis[i]//1, 2)
    res = max(lis)-min(lis)
    print(lis)
    print(res)

max_min_tails(creat_rand_list())
