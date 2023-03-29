# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (
# т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

min, max = 0, 100
list_1 = [randint(min, max) for _ in range(int(input("Введите длинну массива: ")))]
print(list_1)

min_border = int(input("Введите нижнюю границу: "))
max_border = int(input("Введите верхнюю границу: "))

list_2 = []
for i in range(len(list_1)):
    if min_border <= list_1[i] <= max_border:
        list_2.append(i)
print(list_2)
