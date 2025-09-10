import os
import time

from utils import rand_bool
from utils import rand_cell
from utils import rand_neighbour

# 0 - field
# 1 - tree
# 2 - river
# 3 - hospital
# 4 - upgrade

# 🌳🟨🔥🚁🌊🏥⛪⬛

CELL_TYPES = "🟩🌳🌊🏥⛪🔥🚁☁️️🌧"

TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 1000

class Map:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.cells = [[0 for i in range(self.width)] for j in range(self.height)]

        self.generate_forest(3, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_update_shop()
        self.generate_hospital()

    def check_bounds(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True

    def print_map(self, helicopter, clouds):
        print('🟨' * (self.width + 2))
        for ri in range(self.height):
            print('🟨', end='')
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if clouds.cells[ri][ci] == 1:
                    print('◻️', end='')
                elif clouds.cells[ri][ci] == 2:
                    print('🟥', end='')
                elif helicopter.y == ri and helicopter.x == ci:
                    print('🚁', end='')
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            print('🟨')
        print('🟨' * (self.width + 2))

    def generate_river(self, l):
        rx, ry = rand_cell(self.width, self.height)
        self.cells[ry][rx] = 2
        while l > 0:
            nrx, nry = rand_neighbour(rx, ry)
            if self.check_bounds(nrx, nry) and self.cells[nry][nrx] != 2:
                self.cells[ry][rx] = 2
                rx, ry = nrx, nry
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.height):
            for ci in range(self.width):
                if rand_bool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        cx, cy = rand_cell(self.width, self.height)
        if self.cells[cy][cx] == 0:
            self.cells[cy][cx] = 1

    def generate_update_shop(self):
        cx, cy = rand_cell(self.width, self.height)
        self.cells[cy][cx] = 3

    def generate_hospital(self):
        cx, cy = rand_cell(self.width, self.height)
        if self.cells[cy][cx] == 3:
            self.generate_hospital()
        else:
            self.cells[cy][cx] = 4

    def generate_fire(self):
        cx, cy = rand_cell(self.width, self.height)
        if self.cells[cy][cx] == 1:
            self.cells[cy][cx] = 5

    def update_fires(self):
        for ri in range(self.height):
            for ci in range(self.width):
                if self.cells[ri][ci] == 5:
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.generate_fire()

    def process_helicopter(self, helicopter, clouds):
        c = self.cells[helicopter.y][helicopter.x]
        d = clouds.cells[helicopter.y][helicopter.x]
        if c == 2:
            helicopter.tank = helicopter.tank_capacity
        if c == 5:
            if helicopter.tank > 0:
                helicopter.tank -= 1
                helicopter.score += TREE_BONUS
                self.cells[helicopter.y][helicopter.x] = 1
        if c == 4 and helicopter.score >= UPGRADE_COST:
            helicopter.score -= UPGRADE_COST
            helicopter.tank_capacity += 1
        if c == 6 and helicopter.score >= LIFE_COST:
            helicopter.score -= LIFE_COST
            helicopter.lives += 10
        if d == 2:
            helicopter.lives -= 1
            if helicopter.lives <= 0:
                helicopter.game_over()

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"]

