import os
import time

from utils import rand_cell


class Helicopter:
    def __init__(self, w, h):
        self.x, self.y = rand_cell(w, h)
        self.w, self.h = w, h
        self.tank = 0
        self.tank_capacity = 1
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if 0 <= nx < self.w and 0 <= ny < self.h:
            self.x = nx
            self.y = ny

    def print_stats(self):
        print("tank: {0}/{1} | score: {2} | lives: {3} | hel: {4}:{5}".format(self.tank, self.tank_capacity, self.score,
                                                                              self.lives, self.x, self.y))

    def game_over(self):
        os.system('clear')
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("                             ")
        print("Game over. Your score is {0}".format(self.score))
        print("                             ")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)

    def export_data(self):
        return {
            "score": self.score,
            "lives": self.lives,
            "x": self.x,
            "y": self.y,
            "tank": self.tank,
            "tank_capacity": self.tank_capacity
        }

    def import_data(self, data):
        self.score = data["score"]
        self.lives = data["lives"]
        self.x = data["x"]
        self.y = data["y"]
        self.tank = data["tank"]
        self.tank_capacity = data["tank_capacity"]
