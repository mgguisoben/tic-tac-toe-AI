import pygame

PLAYER_COLOR = "green"
COM_COLOR = "red"


class Marker:

    def __init__(self, screen, coord, turn, cell_size):
        self.screen = screen
        self.coord = coord
        self.turn = turn

        self.marker = pygame.Surface(cell_size).convert_alpha()
        self.marker.fill([0, 0, 0, 0])
        self.rect = self.marker.get_rect()

        self.create_marker()

    def create_marker(self):
        self.rect.topleft = self.coord

        if self.turn == 1:
            pygame.draw.line(self.marker, PLAYER_COLOR, (40, 40), (160, 160), 20)
            pygame.draw.line(self.marker, PLAYER_COLOR, (160, 40), (40, 160), 20)
        else:
            pygame.draw.circle(self.marker, COM_COLOR, (100, 100), 70, 15)

    def draw(self):
        self.screen.blit(self.marker, self.rect)
