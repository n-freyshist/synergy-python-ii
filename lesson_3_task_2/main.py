# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов.
# Он должен запрашивать по порядку этапы развития человека и в конце вывести все стадии,
# разделенные знаком =>, что будет означать постепенный переход от одного к другому.

GREETINGS_TEXT = "Назови 4 этапа развития человека:"
HINT_STAGE_1 = "Первый этап:"
HINT_STAGE_2 = "Второй этап:"
HINT_STAGE_3 = "Третий этап:"
HINT_STAGE_4 = "Четвертый этап:"

print(GREETINGS_TEXT)
print(HINT_STAGE_1)
stage_1 = input()

print(HINT_STAGE_2)
stage_2 = input()

print(HINT_STAGE_3)
stage_3 = input()

print(HINT_STAGE_4)
stage_4 = input()

print(stage_1, stage_2, stage_3, stage_4, sep="+")
