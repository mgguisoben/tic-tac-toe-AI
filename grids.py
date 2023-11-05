import pygame as pg

GRID_COLOR = "#4E6E81"


class Grids:

    def __init__(self, window, window_length):
        self.window = window
        self.length = window_length

    def create_grids(self):
        for x in range(3):
            start = (200 * x, 0)
            end = (200 * x, self.length)
            pg.draw.line(self.window, GRID_COLOR, start, end, 5)
            pg.draw.line(self.window, GRID_COLOR, start[::-1], end[::-1], 5)
