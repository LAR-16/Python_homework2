# Задача 14 про степени 2-ки

import math
number = int(input("Введите число: "))
for i in range(number):
    if math.pow(2, i) < number:
        print(math.trunc(math.pow(2, i)))
