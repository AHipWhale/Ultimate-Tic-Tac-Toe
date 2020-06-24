import random

from Game import checkForGridWin, checkForFullGrid, checkForEmptyGrid

current_state = [[],[],[]]

def gridForAi(grid):
    """Deze functie brengt de grid in kaart voor het Ai algoritme."""
    global current_state
    for firstGrids in range(0,3):
        current_state[0].append(grid[firstGrids])
    for middleGrids in range(3,6):
        current_state[1].append(grid[middleGrids])
    for lastGrids in range(6,9):
        current_state[2].append(grid[lastGrids])


def max_alpha_beta(grid, alpha, beta):
    """Deze functie is de eerste helft van het minimax alpha beta pruning algoritme"""
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

                if maxv >= beta:
                    return (maxv, px, py)

                if maxv > alpha:
                    alpha = maxv

    return (maxv, px, py)


def min_alpha_beta(grid, alpha, beta):
    """Deze functie is de tweede helft van het minimax alpha beta pruning algoritme"""
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

def play_alpha_beta(grid, allGrids):
    """Deze functie roept het minimax algoritme op.
      Om verandering te brengen in de keuzen, heb ik ervoor gezorgt dat de eerste keuze in een grid random is,
      maar niet een vak die lijd naar een volle grid. Als de speler de Ai naar een vol vak stuurt kiest de Ai een random
      grid om daar zijn keuze in te maken"""
    global player_turn, current_state
    if checkForFullGrid(grid) == True:
        while True:
            chosenGrid = random.choice(allGrids)
            resultOfCheck = checkForFullGrid(chosenGrid)
            if resultOfCheck != True:
                break
    else:
        chosenGrid = grid

    gridForAi(chosenGrid)

    if checkForEmptyGrid(grid) == True:
        while True:
            px = random.randint(0, 2)
            py = random.randint(0, 2)
            if checkForFullGrid(getNextGrid([px, py], allGrids)) != True:
                break
    else:
        (m, px, py) = max_alpha_beta(chosenGrid, -2, 2)

    current_state[px][py]['text'] = 'O'
    current_state = [[], [], []]
    return px, py

def getNextGrid(grid, allGrids):
    """Deze fucntie brengt in kaart, wat de volgende grid is waar in gespeelt moet worden."""
    cordsList = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]]
    cordinaten = cordsList[int(grid[0])][int(grid[1])]
    return allGrids[cordinaten]