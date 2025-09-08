# Пользователь вводит целое число.
# Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число".
# Например, численным описанием числа 190 является строка "положительное четное число".
# Если число не является четным - выведите сообщение "число не является четным".

GREETINGS_TEXT = "Введите целое число:"
RESULT_TEXT = "Введено %s %s число."
RESULT_ZERO_TEXT = "Введен ноль."
RESULT_ODD_NUMBER_TEXT = "Число не является четным."

EVEN = "четное"
ODD = "нечетное"
POSITIVE = "положительное"
NEGATIVE = "отрицательное"

print(GREETINGS_TEXT)
n = int(input())

if n == 0:
    print(RESULT_ZERO_TEXT)
else:
    is_even = n % 2 == 0
    is_positive = n > 0
    print(RESULT_TEXT % (POSITIVE if is_positive else NEGATIVE, EVEN if is_even else ODD))
    if not is_even:
        print(RESULT_ODD_NUMBER_TEXT)


