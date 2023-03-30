# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
my_list = []
n = int(input('Введите количество элементов массива: '))
for _ in range(n):
    my_list.append(random.randint(1,10))
print(my_list)

min_el = int(input('Введите минимум диапазона: '))
max_el = int(input('Введите максимум диапазона: '))

print('Индексы элементов по заданному условию: ')
indexsi = []
for i in range(len(my_list)):
    if (my_list[i]>min_el) and (my_list[i]<max_el):
        print(i, end=' ')