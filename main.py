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
    return pos_x, pos_y


def remove_marked_cell(pos):
    cell_index = cell_coordinates.index(pos)
    cells_dict.pop(cell_index)

    return cell_index


def update_game_state(mark, i):
    game_state[i + 1] = mark


def check_winner(state, mark):
    if state[1] == state[2] and state[1] == state[3] and state[1] == mark:
        return False
    elif state[4] == state[5] and state[4] == state[6] and state[4] == mark:
        return False
    elif state[7] == state[8] and state[7] == state[9] and state[7] == mark:
        return False
    elif state[1] == state[4] and state[1] == state[7] and state[1] == mark:
        return False
    elif state[2] == state[5] and state[2] == state[8] and state[2] == mark:
        return False
    elif state[3] == state[6] and state[3] == state[9] and state[3] == mark:
        return False
    elif state[1] == state[5] and state[1] == state[9] and state[1] == mark:
        return False
    elif state[7] == state[5] and state[7] == state[3] and state[7] == mark:
        return False
    else:
        return True


def check_draw():
    for key in game_state.keys():
        if game_state[key] == 0:
            return False
    return True


def next_move():
    best_score = -1000
    best_move = 0

    for key, value in game_state.items():
        if value == 0:
            game_state[key] = 1
            score = minimax(False)
            game_state[key] = 0
            if score > best_score:
                best_score = score
                best_move = key

    return best_move - 1


def minimax(is_maximizing):
    if check_winner(game_state, mark=1):
        return -1
    elif check_winner(game_state, mark=-1):
        return 1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -1000
        for key, value in game_state.items():
            if value == 0:
                game_state[key] = 1
                score = minimax(False)
                game_state[key] = 0
                if score > best_score:
                    best_score = score

        return best_score
    else:
        best_score = 1000
        for key, value in game_state.items():
            if value == 0:
                game_state[key] = 1
                score = minimax(True)
                game_state[key] = 0
                if score < best_score:
                    best_score = score

        return best_score


# Main WINDOW
pg.init()
pg.display.set_caption("TicTacToe")
window = pg.display.set_mode((WIN_DIM, WIN_DIM))

cell_coordinates = [(200 * i, 200 * j) for i in range(3) for j in range(3)]
cells_dict = {index: Cells(window, CELL_DIM, coord) for index, coord in enumerate(cell_coordinates)}

markers = []

game_state = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

player = 1
running = True

while running:

    window.fill(BG_COLOR)

    for event in pg.event.get():
        if check_winner(game_state, 1):
            running = False
        if check_winner(game_state, -1):
            running = False

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

                new_pos = cell_coordinates[next_move()]
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

    running = not check_draw()
    # running = check_winner(game_state, 1)
    # running = check_winner(game_state, 2)

pg.quit()
