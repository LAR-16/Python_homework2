# Задача 10 про монетки
import random
N = int(input("Введите число монеток: "))
heads = 0
tails = 0
for _ in range(N):
    num = (random.randint(0, 1))
    print(num)
    if num == 0:
        heads += 1
    elif num == 1:
        tails += 1
print()
if heads > tails:
    print(f'Нужно перевернуть {tails} монеток')
else:
    print(f'Нужно перевернуть {heads} монеток')
