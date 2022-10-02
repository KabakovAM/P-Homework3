# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

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

def product_pair_numbers(lis):
    lg = len(lis)
    new_lis = []
    for i in range(lg//2):
        new_lis.append(lis[i]*lis[lg-i-1])
    if lg % 2 != 0:
        new_lis.append(lis[lg//2])
    print(lis)
    print(new_lis)

product_pair_numbers(creat_rand_list())
