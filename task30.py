# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input("Введите первый член: "))
d = int(input("Введите шаг: "))
n = int(input("Введите кол-во элемемнтов: "))

list_1 = []
for i in range(1, n + 1):
    list_1.append(a1 + (i - 1) * d)
print(list_1)