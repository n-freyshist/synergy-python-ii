# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв?
# Для решения задачи создайте переменную и в неё положите слово с помощью input().
# Определите количество каждой из этих гласных букв.
# Если какой-то из перечисленных букв нет - Выведите False.

print("Введите слово из маленьких латинских букв")
word = input()

counter_a = 0
counter_e = 0
counter_i = 0
counter_o = 0
counter_u = 0
counter_y = 0

for i in word:
    if i == 'a':
        counter_a += 1
    elif i == 'e':
        counter_e += 1
    elif i == 'i':
        counter_i += 1
    elif i == 'o':
        counter_o += 1
    elif i == 'u':
        counter_u += 1
    elif i == 'y':
        counter_y += 1

print("a: %s" % (str(counter_a) if counter_a > 0 else "False"))
print("e: %s" % (str(counter_e) if counter_e > 0 else "False"))
print("i: %s" % (str(counter_i) if counter_i > 0 else "False"))
print("o: %s" % (str(counter_o) if counter_o > 0 else "False"))
print("u: %s" % (str(counter_u) if counter_u > 0 else "False"))
print("y: %s" % (str(counter_y) if counter_y > 0 else "False"))