import math
import random
from Game import checkForGridWin, checkForAiTie, checkForFullGrid

def bestMove(grid):
    maxv = -math.inf

    keuzeVak = None

    # tie = checkForAiTie(grid)
    # result = checkForGridWin(grid)

    # if result == 'X':
    #     return (-1, 0)
    # elif result == 'O':
    #     return (1, 0)
    # elif tie == True:
    #     return (0, 0)

    for vak in grid:
        if vak['text'] == ' ':
            vak['text'] = 'O'
            score = minimax(grid, 0, False)
            vak['text'] = ' '
            # print('max_hier')
            if score > maxv:
                maxv = score
                keuzeVak = vak
    keuzeVak['text'] = 'O'

def minimax(grid, depth, isMaximizing, alpha = -math.inf, beta = math.inf):
    # tie = checkForAiTie(grid)
    result = checkForGridWin(grid)
    if result is not None:
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        elif result == 'tie':
            return 0
    if isMaximizing == True:
        bestScore = -math.inf
        for vak in grid:
            if vak['text'] == ' ':
                vak['text'] = 'X'
                score = minimax(grid, depth+1, False, alpha, beta)
                vak['text'] = ' '
                bestScore = max(score, bestScore)
                alpha = max(alpha, score)
                if beta >= alpha:
                    pass
        return bestScore
    else:
        bestScore = math.inf
        for vak in grid:
            if vak['text'] == ' ':
                vak['text'] = 'O'
                score = minimax(grid, depth + 1, True, alpha, beta)
                vak['text'] = ' '
                bestScore = min(score, bestScore)
                beta = min(beta, score)
                    # keuzeVak = vak
                if alpha >= beta:
                    pass
        return bestScore
    # minv = 2
    #
    # keuzeVak = None
    #
    # tie = checkForAiTie(grid)
    # result = checkForGridWin(grid)
    #
    # if result == 'X':
    #     return (-1, 0)
    # elif result == 'O':
    #     return (1, 0)
    # elif tie == True:
    #     return (0, 0)
    #
    # for vak in grid:
    #     if vak['text'] == ' ':
    #         vak['text'] = 'X'
    #         (m, max_i) = Max(grid)
    #         # print('min_hier')
    #         if m < minv:
    #             minv = m
    #             keuzeVak = vak
    #         vak['text'] = ' '
    # return minv, keuzeVak

# def play(grid, allGrids):
#     if checkForFullGrid(grid) == True:
#         while True:
#             chosenkey = random.choice(list(allGrids))
#             chosenGrid = allGrids[chosenkey]
#             resultOfCheck = checkForFullGrid(chosenGrid)
#             if resultOfCheck != True:
#                 break
#     else:
#         chosenGrid = grid
#     print(chosenGrid)
#     (m, keuzeVak) = Max(chosenGrid)
#     keuzeVak['text'] = 'O'
#     return keuzeVak