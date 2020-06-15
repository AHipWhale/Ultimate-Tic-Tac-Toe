from tkinter import *

import tkinter.messagebox
firstMove = True

def checkForWin(grid):
    button1 = grid[0]
    button2 = grid[1]
    button3 = grid[2]
    button4 = grid[3]
    button5 = grid[4]
    button6 = grid[5]
    button7 = grid[6]
    button8 = grid[7]
    button9 = grid[8]

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
          button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
            # tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player A Wins")
        return "X"

        # elif flag == 8:
        #     tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player B Wins")
        return "O"

def denyAcces(allGrids):
    for grid in allGrids:
        for ding in grid:
            ding["state"] = DISABLED

def allowAcces(allGrids):
    for grid in allGrids:
        for ding in grid:
            ding["state"] = NORMAL
            ding["bg"] = "gray"

def changeAcces(nextGrid, allGrids):
    denyAcces(allGrids)
    for ding in nextGrid:
        ding["state"] = NORMAL

def checkForFullGrid(nextGrid):
    full = set()
    for ding in nextGrid:
        full.add(ding["text"])
    if len(full) == 1 and full != {' '}:
        return True