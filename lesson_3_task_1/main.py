# Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники.
# Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца,
# его возраст и кличку, а потом выведет все эти данные в одно предложение. Например:
#
# Это желторотый питон по кличке "Каа". Возраст: 34 года.

GREETINGS_TEXT = "Заполните информацию о вашем питомце"
HINT_ANIMAL_TYPE = "Вид:"
HINT_ANIMAL_AGE = "Возраст:"
HINT_ANIMAL_NAME = "Имя:"
SUMMARY = 'Это %s по кличке "%s". Возраст: %d %s.'


def incline(amount, nom, gen, gen_pl):
    reminder100 = amount % 100
    if 5 <= reminder100 <= 20:
        return gen_pl
    reminder10 = reminder100 % 10
    if reminder10 == 1:
        return nom
    if 2 <= reminder10 <= 4:
        return gen
    return gen_pl


print(GREETINGS_TEXT)
print(HINT_ANIMAL_TYPE)
animal_type = input()

print(HINT_ANIMAL_AGE)
animal_age = int(input())

print(HINT_ANIMAL_NAME)
animal_name = input()

print(SUMMARY % (animal_type, animal_name, animal_age, incline(animal_age, "год", "года", "лет")))
