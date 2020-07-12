# This script by Dmitriy Morozov
#
#   _________________________________
#   Version 1
#
#   2020
#
#   _________________________________


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# на вход номер, на вывод значение


def fibonachi(i):  # методом рекурсии
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonachi(i - 1) + fibonachi(i - 2)


def fibonachi_1(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        array = []
        array.append(0)
        array.append(1)
        for number in range(2, i + 1):
            array.append(number)
            array[number] = array[number - 2] + array[number - 1]
        return array[i]


x = int(input("Введите индекс числа Фибоначчи: "))

print("Результат, полученный методом использования массива: " + str(fibonachi_1(x)))
print("Результат, полученный методом рекурсии: " + str(fibonachi(x)))
