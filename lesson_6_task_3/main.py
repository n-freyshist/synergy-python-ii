# Вводятся целые числа A и B. Гарантируется, что A ≤ B.
# Выведите все четные числа на заданном отрезке через пробел.

print("Введи A:")
a = int(input())

print("Введи B (должно быть больше либо равно A):")
b = int(input())

even_numbers = []
for i in range(a, b+1):
    if i % 2 == 0:
        even_numbers.append(i)

print(' '.join(map(str, even_numbers)))


