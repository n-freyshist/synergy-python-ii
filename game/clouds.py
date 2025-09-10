from utils import rand_bool


class Clouds:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for x in range(width)] for y in range(height)]

    def update(self, r = 1, mxr = 10, g = 1, mxg = 10):
        for row in range(self.height):
            for col in range(self.width):
                if rand_bool(r,mxr):
                    self.cells[row][col] = 1
                    if rand_bool(g,mxg):
                        self.cells[row][col] = 2
                else:
                    self.cells[row][col] = 0

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"]