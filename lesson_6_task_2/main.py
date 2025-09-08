# Вводится натуральное число X.
# Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда).

print("Введи X:")
x = int(input())

dividers_counter = 0
for i in range(1, x+1):
    if x / i == x // i:
        dividers_counter += 1

print(dividers_counter)