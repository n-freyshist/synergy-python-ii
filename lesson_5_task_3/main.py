# Два инвестора - Майкл и Иван хотят вложиться в стартап.
# Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно.
# У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike,
# если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

print("Сколько денег у Майкла?")
michael_money = int(input())

print("Сколько денег у Ивана?")
john_money = int(input())

print("Сколько денег требуют инвесторы?")
min_investment = int(input())

if michael_money >= min_investment:
    if john_money >= min_investment:
        print("2")
    else:
        print("Mike")
elif john_money >= min_investment:
    print("Ivan")
else:
    if michael_money + john_money >= min_investment:
        print(1)
    else:
        print(0)
