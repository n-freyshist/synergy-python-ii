# Сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте, сколько из них равны нулю, и выведите это количество.

print("Введи N:")
n = int(input())

zero_counter = 0
for i in range(n):
    print("Введи число #%d:" % (i+1))
    a = int(input())
    if a == 0:
        zero_counter += 1

print(zero_counter)