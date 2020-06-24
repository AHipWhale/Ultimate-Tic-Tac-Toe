from Game import checkForGridWin

current_state = [[],[],[]]

def gridForAi(grid):
    global current_state
    for firstGrids in range(0,3):
        current_state[0].append(grid[firstGrids])
    for middleGrids in range(3,6):
        current_state[1].append(grid[middleGrids])
    for lastGrids in range(6,9):
        current_state[2].append(grid[lastGrids])


def max_alpha_beta(grid, alpha, beta):
    maxv = -2
    px = None
    py = None

    result = checkForGridWin(grid, True)

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == ' ':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if current_state[i][j]['text'] == ' ':
                current_state[i][j]['text'] = 'O'
                (m, min_i, in_j) = min_alpha_beta(grid, alpha, beta)
                if m > maxv:
                    maxv = m
                    px = i
                    py = j
                current_state[i][j]['text'] = ' '

                # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                if maxv >= beta:
                    return (maxv, px, py)

                if maxv > alpha:
                    alpha = maxv

    return (maxv, px, py)


def min_alpha_beta(grid, alpha, beta):
    minv = 2

    qx = None
    qy = None

    result = checkForGridWin(grid, True)

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == ' ':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if current_state[i][j]['text'] == ' ':
                current_state[i][j]['text'] = 'X'
                (m, max_i, max_j) = max_alpha_beta(grid, alpha, beta)
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                current_state[i][j]['text'] = ' '

                if minv <= alpha:
                    return (minv, qx, qy)

                if minv < beta:
                    beta = minv

    return (minv, qx, qy)

def play_alpha_beta(grid):
    global player_turn, current_state
    gridForAi(grid)
    # draw_board()

    (m, px, py) = max_alpha_beta(grid, -2, 2)
    current_state[px][py]['text'] = 'O'
    current_state = [[], [], []]