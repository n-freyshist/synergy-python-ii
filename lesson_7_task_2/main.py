# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один.
# Выведите измененную строку.

print("Введи строку:")
s = input()
res = ""
last_symbol_is_space = False

for symbol in s:
    current_symbol_is_space = symbol == " "

    if current_symbol_is_space:
        if last_symbol_is_space:
            continue
    res += symbol
    last_symbol_is_space = current_symbol_is_space

print(res)