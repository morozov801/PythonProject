# This script by Dmitriy Morozov
#
#   _________________________________
#   Version 1
#
#   2020
#
#   _________________________________

import random


def bin_search(new_list, x, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        print("start = " + str(start), "midle = " + str(mid), "stop = " + str(stop) + "\n")
        if new_list[mid] > x:
            return bin_search(new_list, x, start, mid - 1)
        elif new_list[mid] < x:
            return bin_search(new_list, x, mid + 1, stop)
        else:
            return mid


mylist = [1, 3, 11, 22, 34, 40, 51, 63, 70, 99, 111]  # инициализируем массив с числами
value = 99
mylist.sort()  # сортируем массив с числами
print("Исходный массив: " + str(mylist) + "\nЧисло для поиска: " + str(value))  # выводим массив чисел

start = 0
stop = len(mylist)

x = bin_search(mylist, value, start, stop)
if x == False:
    print("Такого числа в массиве нет")
else:
    print("Число " + str(value) + " находится в массиве под индексом " + str(x))

# for i in range (0, 29):
#    mas.append(random.randint(-100, 100))
