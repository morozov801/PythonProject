# This script by Dmitriy Morozov
#
#   _________________________________
#   Version 1
#
#   2020
#
#   _________________________________


def function1 (x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * function1(x - 1)


def function2(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + function2(x - 1)


print("This program use recursion in worker!")

x = input("Please, enter number: ")
y = input("Enter operation. + or * : ")
value = int(x)
if y == "*":
    print(function1(int(x)))
elif y == "+":
    print(function2(int(x)))
else:
    print("Invalid arguments")
