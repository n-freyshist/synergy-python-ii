# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
class CashBox:
    def __init__(self):
        self.total = 0

    def top_up(self, amount):
        self.total += amount

    def count_1000(self):
        return self.total // 1000

    def take_away(self, x):
        if x > self.total:
            raise ValueError("Недостаточно денег")
        self.total -= x