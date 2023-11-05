import pygame as pg

HOVER_COLOR = "gray"


class Cells:

    def __init__(self, window, cell_dim, coordinate):
        self.window = window

        self.cell_normal = pg.Surface(cell_dim).convert_alpha()
        self.cell_normal.fill([0, 0, 0, 0])

        self.cell_hovered = pg.Surface(cell_dim)
        self.cell_hovered.fill(HOVER_COLOR)

        self.cell = self.cell_normal
        self.rect = self.cell.get_rect()
        self.rect.topleft = coordinate

        self.hovered = False

    def draw(self):
        self.window.blit(self.cell, self.rect)

    def update(self):

        if self.hovered:
            self.cell = self.cell_hovered
        else:
            self.cell = self.cell_normal

    def handle_event(self, event):

        if event.type == pg.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
