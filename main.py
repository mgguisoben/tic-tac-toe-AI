import random

import pygame as pg

from cells import Cells
from grids import Grids
from marker import Marker

BG_COLOR = "white"
WIN_DIM = 600
CELL_DIM = tuple([WIN_DIM / 3] * 2)


def get_mouse_pos():
    pos = pg.mouse.get_pos()
    pos_x = pos[0] // 200 * 200
    pos_y = pos[1] // 200 * 200
    return (pos_x, pos_y)


def remove_marked_cell():
    cell_index = cell_coordinates.index(new_pos)
    cells_dict.pop(cell_index)
    game_state[cell_index] = player
    cell_x = cell_index // 3
    cell_y = cell_index % 3
    return cell_x, cell_y


def check_winner(board):
    if (board[0] == [1, 1, 1] or board[1] == [1, 1, 1] or board[2] == [1, 1, 1] or
            (board[0][0] == 1 and board[1][0] == 1 and board[2][0]) == 1 or
            (board[0][1] == 1 and board[1][1] == 1 and board[2][1]) == 1 or
            (board[0][2] == 1 and board[1][2] == 1 and board[2][2]) == 1 or
            (board[0][0] == 1 and board[1][1] == 1 and board[2][2]) == 1 or
            (board[0][2] == 1 and board[1][1] == 1 and board[2][0]) == 1):
        return False
    else:
        return True


def next_move():
    open_cells = []
    for index, item in enumerate(game_state):
        if item == 0:
            open_cells.append(index)

    return random.choice(open_cells)


# Main WINDOW
pg.init()
pg.display.set_caption("TicTacToe")
window = pg.display.set_mode((WIN_DIM, WIN_DIM))

cell_coordinates = [(200 * i, 200 * j) for i in range(3) for j in range(3)]
cells_dict = {index: Cells(window, CELL_DIM, coord) for index, coord in enumerate(cell_coordinates)}

markers = []

player_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
com_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

player = 1
running = True

while running:

    window.fill(BG_COLOR)

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN and player == 1:
            try:

                # Get MOUSE Coordinates
                new_pos = get_mouse_pos()
                x, y = remove_marked_cell()

                player_board[x][y] = player

                marker = Marker(window, new_pos, player, CELL_DIM)
                markers.append(marker)

                player *= -1

                running = check_winner(player_board)



            except KeyError:
                continue

        elif event.type == pg.MOUSEBUTTONUP and player == -1:
            try:

                new_pos = cell_coordinates[next_move()]
                x, y = remove_marked_cell()

                com_board[x][y] = player * -1

                marker = Marker(window, new_pos, player, CELL_DIM)
                markers.append(marker)

                player *= -1

                running = check_winner(com_board)

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

    # Create GRIDS
    grids = Grids(window, WIN_DIM)
    grids.create_grids()

    pg.display.update()

pg.quit()
