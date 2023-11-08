import pygame as pg

from ai import AI
from cells import Cells
from grids import Grids
from marker import Marker

import time

BG_COLOR = "#F9DBBB"
WIN_DIM = 600
CELL_DIM = tuple([WIN_DIM / 3] * 2)


def get_mouse_pos():
    pos = pg.mouse.get_pos()
    pos_x = pos[0] // 200 * 200
    pos_y = pos[1] // 200 * 200
    return pos_x, pos_y


def remove_marked_cell(pos):
    cell_index = cell_coordinates.index(pos)
    cells_dict.pop(cell_index)

    return cell_index


def update_game_state(mark, i):
    game_state[i + 1] = mark






pg.init()
pg.display.set_caption("TicTacToe")
window = pg.display.set_mode((WIN_DIM, WIN_DIM))

font = pg.font.Font("assets/font/ShellMuseum.ttf", 100)

cell_coordinates = [(200 * i, 200 * j) for i in range(3) for j in range(3)]
cells_dict = {index: Cells(window, CELL_DIM, coord) for index, coord in enumerate(cell_coordinates)}

markers = []

game_state = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

ai = AI(game_state)

player = 1

game_over_text = ""

running = False
game_start = False
game_over = False

while not game_start:

    window.fill(BG_COLOR)

    game_title_text = "TicTacToe"
    game_title_img = font.render(game_title_text, False, 'black')
    game_title_rect = game_title_img.get_rect()
    game_title_rect.center = (300, 200)
    window.blit(game_title_img, game_title_rect)

    start_button_pos = (300, 350)
    start_button = pg.image.load("assets/images/play-button.png")
    start_button = pg.transform.scale(start_button, (200, 200))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = start_button_pos
    window.blit(start_button, start_button_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_start = True
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = get_mouse_pos()
            if pos == (200, 200):
                running = True
                game_start = True

    pg.display.update()

while running:

    window.fill(BG_COLOR)

    if ai.check_winner(1):
        game_over_text = "-X- won"
        time.sleep(1)
        running = False
        game_over = True
    elif ai.check_winner(-1):
        game_over_text = "-O- won"
        time.sleep(1)
        running = False
        game_over = True
    elif ai.check_draw():
        game_over_text = "Draw"
        time.sleep(1)
        running = False
        game_over = True


    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN and player == 1:
            try:
                new_pos = get_mouse_pos()
                removed = remove_marked_cell(new_pos)

                update_game_state(player, removed)

                marker = Marker(window, new_pos, player, CELL_DIM)
                markers.append(marker)

                player *= -1

            except KeyError:
                continue

        elif event.type == pg.MOUSEBUTTONUP and player == -1:
            try:

                new_pos = cell_coordinates[ai.next_move()]
                removed = remove_marked_cell(new_pos)

                update_game_state(player, removed)

                marker = Marker(window, new_pos, player, CELL_DIM)
                markers.append(marker)

                player *= -1

            except KeyError:
                continue

        for cell in cells_dict.values():
            cell.handle_event(event)

    for cell in cells_dict.values():
        cell.update()

    for cell in cells_dict.values():
        cell.draw()

    for marker in markers:
        marker.draw()

    grids = Grids(window, WIN_DIM)
    grids.create_grids()

    pg.display.update()

while game_over:

    window.fill(BG_COLOR)

    game_title_text = game_over_text
    game_title_img = font.render(game_title_text, False, 'black')
    game_title_rect = game_title_img.get_rect()
    game_title_rect.center = (300, 200)
    window.blit(game_title_img, game_title_rect)

    start_button_pos = (300, 350)
    start_button = pg.image.load("assets/images/play-button.png")
    start_button = pg.transform.scale(start_button, (200, 200))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = start_button_pos
    window.blit(start_button, start_button_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_start = False

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = get_mouse_pos()
            if pos == (200, 200):
                game_over = False
                running = True

    pg.display.update()

pg.quit()
