import pygame as pg

from ai import AI
from cells import Cells
from grids import Grids
from marker import Marker

BG_COLOR = "#F9DBBB"
WIN_DIM = 600
CELL_DIM = tuple([WIN_DIM / 3] * 2)
GAME_TITLE = "TicTacToe"


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


def title_screen(text):
    window.fill(BG_COLOR)

    game_text = font.render(text, False, 'black')
    game_text_rect = game_text.get_rect()
    game_text_rect.center = (300, 200)
    window.blit(game_text, game_text_rect)

    start_button_pos = (300, 350)
    start_button = pg.image.load("assets/images/play-button.png")
    start_button = pg.transform.scale(start_button, (200, 200))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = start_button_pos
    window.blit(start_button, start_button_rect)


def game_over():
    global game_over_text
    if ai.check_winner(1):
        game_over_text = "-X- won"
        return True
    elif ai.check_winner(-1):
        game_over_text = "-O- won"
        return True
    elif ai.check_draw():
        game_over_text = "Draw"
        return True
    return False


pg.init()
pg.display.set_caption(GAME_TITLE)
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

while not game_start:

    title_screen(GAME_TITLE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_start = True
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = get_mouse_pos()
            if pos == (200, 200):
                game_start = True
                running = True

    pg.display.update()

while running:

    window.fill(BG_COLOR)

    grids = Grids(window, WIN_DIM)
    grids.create_grids()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if not game_over():
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

            pg.display.update()

        elif game_over():

            title_screen(game_over_text)

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = get_mouse_pos()
                if pos == (200, 200):
                    markers = []
                    cells_dict = {index: Cells(window, CELL_DIM, coord) for index, coord in enumerate(cell_coordinates)}
                    game_state = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
                    player = 1
                    ai = AI(game_state)

            pg.display.update()

pg.quit()
