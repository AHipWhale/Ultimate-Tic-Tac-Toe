from tkinter import *
import tkinter.messagebox

grid1 = None
grid2 = None
grid3 = None
grid4 = None
grid5 = None
grid6 = None
grid7 = None
grid8 = None
grid9 = None

flag = 0

def checkForGridWin(grid, checkforAi):
    global flag

    if (grid[0]['text'] == 'X' and grid[1]['text'] == 'X' and grid[2]['text'] == 'X' or
          grid[3]['text'] == 'X' and grid[4]['text'] == 'X' and grid[5]['text'] == 'X' or
          grid[6]['text'] == 'X' and grid[7]['text'] == 'X' and grid[8]['text'] == 'X' or
          grid[0]['text'] == 'X' and grid[3]['text'] == 'X' and grid[6]['text'] == 'X' or
          grid[1]['text'] == 'X' and grid[4]['text'] == 'X' and grid[7]['text'] == 'X' or
          grid[2]['text'] == 'X' and grid[5]['text'] == 'X' and grid[8]['text'] == 'X' or
          grid[0]['text'] == 'X' and grid[4]['text'] == 'X' and grid[8]['text'] == 'X' or
          grid[2]['text'] == 'X' and grid[4]['text'] == 'X' and grid[6]['text'] == 'X'):
        flag += 1
        return "X"

    elif (grid[0]['text'] == 'O' and grid[1]['text'] == 'O' and grid[2]['text'] == 'O' or
          grid[3]['text'] == 'O' and grid[4]['text'] == 'O' and grid[5]['text'] == 'O' or
          grid[6]['text'] == 'O' and grid[7]['text'] == 'O' and grid[8]['text'] == 'O' or
          grid[0]['text'] == 'O' and grid[3]['text'] == 'O' and grid[6]['text'] == 'O' or
          grid[1]['text'] == 'O' and grid[4]['text'] == 'O' and grid[7]['text'] == 'O' or
          grid[2]['text'] == 'O' and grid[5]['text'] == 'O' and grid[8]['text'] == 'O' or
          grid[0]['text'] == 'O' and grid[4]['text'] == 'O' and grid[8]['text'] == 'O' or
          grid[2]['text'] == 'O' and grid[4]['text'] == 'O' and grid[6]['text'] == 'O'):
        flag += 1
        return"O"

    if checkforAi == False:
        if checkForTie(grid):
            return ' '
    else:
        if checkForAiTie(grid):
            return ' '

def checkForTie(grid):
    global flag
    volleVakken = 0
    for vak in grid:
        if vak['text'] == 'O' or vak['text'] == 'X':
            volleVakken+=1
    if volleVakken == 9:
        flag += 1
        for vak in grid:
            vak['text'] = "Tie"
        return True
    else:
        return False

def checkForAiTie(grid):
    global flag
    volleVakken = 0
    for vak in grid:
        if vak['text'] == 'O' or vak['text'] == 'X':
            volleVakken+=1
    if volleVakken == 9:
        flag += 1
        return True
    else:
        return False

def denyAcces(allGrids):
    for grid in allGrids:
        for vak in grid:
            vak["state"] = DISABLED

def allowAcces(allGrids):
    for grid in allGrids:
        for vak in grid:
            vak["state"] = NORMAL
            vak["bg"] = "gray"

def changeAcces(nextGrid, allGrids):
    denyAcces(allGrids)
    for vak in nextGrid:
        vak["state"] = NORMAL

def checkForFullGrid(nextGrid):
    full = set()
    for vak in nextGrid:
        full.add(vak["text"])
    if len(full) == 1 and full != {' '}:
        return True

def checkForEmptyGrid(nextGrid):
    full = set()
    for vak in nextGrid:
        full.add(vak["text"])
    if len(full) == 1 and full == {' '}:
        return True

def defineGrid(allGrids, grid, symbol):
    global grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9
    if allGrids[0] == grid:
        grid1 = symbol
    elif allGrids[1] == grid:
        grid2 = symbol
    elif allGrids[2] == grid:
        grid3 = symbol
    elif allGrids[3] == grid:
        grid4 = symbol
    elif allGrids[4] == grid:
        grid5 = symbol
    elif allGrids[5] == grid:
        grid6 = symbol
    elif allGrids[6] == grid:
        grid7 = symbol
    elif allGrids[7] == grid:
        grid8 = symbol
    else:
        grid9 = symbol

def checkForGameWin(allGrids, grid, symbol, player1, player2):
    global flag
    defineGrid(allGrids, grid, symbol)

    if (grid1 == 'X' and grid2 == 'X' and grid3 == 'X' or
            grid4 == 'X' and grid5 == 'X' and grid6 == 'X' or
            grid7 == 'X' and grid8 == 'X' and grid9 == 'X' or
            grid1 == 'X' and grid4 == 'X' and grid7 == 'X' or
            grid2 == 'X' and grid5 == 'X' and grid8 == 'X' or
            grid3 == 'X' and grid6 == 'X' and grid9 == 'X' or
            grid1 == 'X' and grid5 == 'X' and grid9 == 'X' or
            grid3 == 'X' and grid5 == 'X' and grid7 == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player1.get() + " Wins!")

    elif flag == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (grid1 == 'O' and grid2 == 'O' and grid3 == 'O' or
            grid4 == 'O' and grid5 == 'O' and grid6 == 'O' or
            grid7 == 'O' and grid8 == 'O' and grid9 == 'O' or
            grid1 == 'O' and grid4 == 'O' and grid7 == 'O' or
            grid2 == 'O' and grid5 == 'O' and grid8 == 'O' or
            grid3 == 'O' and grid6 == 'O' and grid9 == 'O' or
            grid1 == 'O' and grid5 == 'O' and grid9 == 'O' or
            grid3 == 'O' and grid5 == 'O' and grid7 == 'O'):
        if type(player2) == tkinter.StringVar:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", player2.get() + " Wins!")
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", player2 + " Wins!")