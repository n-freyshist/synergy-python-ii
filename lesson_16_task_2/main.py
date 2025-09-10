# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она
# перемещается за ход
#
# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий,
# за которое черепашка сможет добраться до x2 y2 от текущей позиции
import math


class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.s = 1

    def go_up(self):
        self.y -= self.s

    def go_down(self):
        self.y += self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Черепашка обессилила и больше не в состоянии двигаться")
        self.s -= 1

    def count_moves(self, x, y):
        abs_x = abs(self.x - x)
        abs_y = abs(self.y - y)
        return round(abs_x / self.s) + round(abs_y / self.s)