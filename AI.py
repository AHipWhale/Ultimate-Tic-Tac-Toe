import random
from Game import checkForGridWin, checkForAiTie, checkForFullGrid

def Max(grid):
    maxv = -2

    keuzeVak = None

    tie = checkForAiTie(grid)
    result = checkForGridWin(grid)

    if result == 'X':
        return (-1, 0)
    elif result == 'O':
        return (1, 0)
    elif tie == True:
        return (0, 0)

    for vak in grid:
        if vak['text'] == ' ':
            vak['text'] = 'O'
            (m, min_i) = Min(grid)
            # print('max_hier')
            if m > maxv:
                maxv = m
                keuzeVak = vak
            vak['text'] = ' '
    return maxv, keuzeVak

def Min(grid):
    minv = 2

    keuzeVak = None

    tie = checkForAiTie(grid)
    result = checkForGridWin(grid)

    if result == 'X':
        return (-1, 0)
    elif result == 'O':
        return (1, 0)
    elif tie == True:
        return (0, 0)

    for vak in grid:
        if vak['text'] == ' ':
            vak['text'] = 'X'
            (m, max_i) = Max(grid)
            # print('min_hier')
            if m < minv:
                minv = m
                keuzeVak = vak
            vak['text'] = ' '
    return minv, keuzeVak

def play(grid, allGrids):
    if checkForFullGrid(grid) == True:
        while True:
            chosenkey = random.choice(list(allGrids))
            chosenGrid = allGrids[chosenkey]
            resultOfCheck = checkForFullGrid(chosenGrid)
            if resultOfCheck != True:
                break
    else:
        chosenGrid = grid
    print(chosenGrid)
    (m, keuzeVak) = Max(chosenGrid)
    keuzeVak['text'] = 'O'
    return keuzeVak