# Задача 12 про 2 числа(Петя и Катя)

sum = int(input("Введите сумму чисел: "))
product = int(input("Введите произведение чисел: "))
x = 1
y = sum-1
while x != sum-1:
    if product == x*y:
        print(f"Первое число = {x}, второе число = {y}")
        break
    else:
        x += 1
        y -= 1
