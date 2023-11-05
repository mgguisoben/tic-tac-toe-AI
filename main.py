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
    cell = cell_coordinates.index(new_pos)
    cells_dict.pop(cell)


# Main WINDOW
pg.init()
pg.display.set_caption("TicTacToe")
window = pg.display.set_mode((WIN_DIM, WIN_DIM))

cell_coordinates = [(200 * i, 200 * j) for i in range(3) for j in range(3)]
cells_dict = {index: Cells(window, CELL_DIM, coord) for index, coord in enumerate(cell_coordinates)}

markers = []

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
                remove_marked_cell()

                marker = Marker(window, new_pos, player, CELL_DIM)
                markers.append(marker)

                player *= -1

            except KeyError:
                continue

        elif event.type == pg.MOUSEBUTTONDOWN and player == -1:
            try:
                # Get MOUSE Coordinates
                new_pos = get_mouse_pos()

                remove_marked_cell()

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

    # Create GRIDS
    grids = Grids(window, WIN_DIM)
    grids.create_grids()

    pg.display.update()

pg.quit()
