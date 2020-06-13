import tkinter.messagebox
import Game
from tkinter import *
import webbrowser

tk = Tk()
tk.title("Ultimate Tic-Tac-Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = ''

bclick = '1'
flag = 0

def btnClick(buttons, next_Grid, this_Grid):
    global bclick, flag, player2_name, player1_name, playerb, pa, grid
    if buttons["text"] == " " and bclick == '1':
        buttons["text"] = "X"
        bclick = '2'
        playerb = p2 + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin(this_Grid)
        nextGrid(next_Grid, this_Grid)
        flag += 1

    elif buttons["text"] == " " and bclick == '2':
        buttons["text"] = "O"
        bclick = '1'
        checkForWin(this_Grid)
        nextGrid(next_Grid, this_Grid)
        flag += 1
    else:
        tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", "Button already Clicked!")

buttons = StringVar()

def gap(row, column):
    # This bit is for the gap between grids
    label = Label(tk, height=1, width=1)
    label.grid(row=row, column=column)

def checkForWin(currentGrid):
    if currentGrid == 1:
        button1 = grid1[0]
        button2 = grid1[1]
        button3 = grid1[2]
        button4 = grid1[3]
        button5 = grid1[4]
        button6 = grid1[5]
        button7 = grid1[6]
        button8 = grid1[7]
        button9 = grid1[8]
    elif currentGrid == 2:
        button1 = grid2[0]
        button2 = grid2[1]
        button3 = grid2[2]
        button4 = grid2[3]
        button5 = grid2[4]
        button6 = grid2[5]
        button7 = grid2[6]
        button8 = grid2[7]
        button9 = grid2[8]
    elif currentGrid == 3:
        button1 = grid3[0]
        button2 = grid3[1]
        button3 = grid3[2]
        button4 = grid3[3]
        button5 = grid3[4]
        button6 = grid3[5]
        button7 = grid3[6]
        button8 = grid3[7]
        button9 = grid3[8]
    elif currentGrid == 4:
        button1 = grid4[0]
        button2 = grid4[1]
        button3 = grid4[2]
        button4 = grid4[3]
        button5 = grid4[4]
        button6 = grid4[5]
        button7 = grid4[6]
        button8 = grid4[7]
        button9 = grid4[8]
    elif currentGrid == 5:
        button1 = grid5[0]
        button2 = grid5[1]
        button3 = grid5[2]
        button4 = grid5[3]
        button5 = grid5[4]
        button6 = grid5[5]
        button7 = grid5[6]
        button8 = grid5[7]
        button9 = grid5[8]
    elif currentGrid == 6:
        button1 = grid6[0]
        button2 = grid6[1]
        button3 = grid6[2]
        button4 = grid6[3]
        button5 = grid6[4]
        button6 = grid6[5]
        button7 = grid6[6]
        button8 = grid6[7]
        button9 = grid6[8]
    elif currentGrid == 7:
        button1 = grid7[0]
        button2 = grid7[1]
        button3 = grid7[2]
        button4 = grid7[3]
        button5 = grid7[4]
        button6 = grid7[5]
        button7 = grid7[6]
        button8 = grid7[7]
        button9 = grid7[8]
    elif currentGrid == 8:
        button1 = grid8[0]
        button2 = grid8[1]
        button3 = grid8[2]
        button4 = grid8[3]
        button5 = grid8[4]
        button6 = grid8[5]
        button7 = grid8[6]
        button8 = grid8[7]
        button9 = grid8[8]
    else:
        button1 = grid9[0]
        button2 = grid9[1]
        button3 = grid9[2]
        button4 = grid9[3]
        button5 = grid9[4]
        button6 = grid9[5]
        button7 = grid9[6]
        button8 = grid9[7]
        button9 = grid9[8]

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif flag == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

def make_Grids():
    H = 2  # hoogte van de knoppen
    W = 4  # breedte van de knoppen
    fg = 'white' # letterkleur
    bg = 'gray' # achtergrondkleur
    font = 'Times 20 bold' # lettertype

    #Buttons of Grid 1
    G1_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button1, 1, 1))
    G1_button1.grid(row=3, column=0)

    G1_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button2, 2, 1))
    G1_button2.grid(row=3, column=1)

    G1_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button3, 3, 1))
    G1_button3.grid(row=3, column=2)

    G1_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button4, 4, 1))
    G1_button4.grid(row=4, column=0)

    G1_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button5, 5, 1))
    G1_button5.grid(row=4, column=1)

    G1_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button6, 6, 1))
    G1_button6.grid(row=4, column=2)

    G1_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button7, 7, 1))
    G1_button7.grid(row=5, column=0)

    G1_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button8, 8, 1))
    G1_button8.grid(row=5, column=1)

    G1_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button9, 9, 1))
    G1_button9.grid(row=5, column=2)

    #Buttons of grid 2
    G2_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button1, 1, 2))
    G2_button1.grid(row=3, column=4)

    G2_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button2, 2, 2))
    G2_button2.grid(row=3, column=5)

    G2_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button3, 3, 2))
    G2_button3.grid(row=3, column=6)

    G2_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button4, 4, 2))
    G2_button4.grid(row=4, column=4)

    G2_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button5, 5, 2))
    G2_button5.grid(row=4, column=5)

    G2_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button6, 6, 2))
    G2_button6.grid(row=4, column=6)

    G2_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button7, 7, 2))
    G2_button7.grid(row=5, column=4)

    G2_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button8, 8, 2))
    G2_button8.grid(row=5, column=5)

    G2_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button9, 9, 2))
    G2_button9.grid(row=5, column=6)

    #Buttons of grid 3
    G3_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button1, 1, 3))
    G3_button1.grid(row=3, column=8)

    G3_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button2, 2, 3))
    G3_button2.grid(row=3, column=9)

    G3_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button3, 3, 3))
    G3_button3.grid(row=3, column=10)

    G3_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button4, 4, 3))
    G3_button4.grid(row=4, column=8)

    G3_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button5, 5, 3))
    G3_button5.grid(row=4, column=9)

    G3_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button6, 6, 3))
    G3_button6.grid(row=4, column=10)

    G3_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button7, 7, 3))
    G3_button7.grid(row=5, column=8)

    G3_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button8, 8, 3))
    G3_button8.grid(row=5, column=9)

    G3_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button9, 9, 3))
    G3_button9.grid(row=5, column=10)

    #Buttons of Grid 4
    G4_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button1, 1, 4))
    G4_button1.grid(row=7, column=0)

    G4_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button2, 2, 4))
    G4_button2.grid(row=7, column=1)

    G4_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button3, 3, 4))
    G4_button3.grid(row=7, column=2)

    G4_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button4, 4, 4))
    G4_button4.grid(row=8, column=0)

    G4_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button5, 5, 4))
    G4_button5.grid(row=8, column=1)

    G4_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button6, 6, 4))
    G4_button6.grid(row=8, column=2)

    G4_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button7, 7, 4))
    G4_button7.grid(row=9, column=0)

    G4_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button8, 8, 4))
    G4_button8.grid(row=9, column=1)

    G4_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button9, 9, 4))
    G4_button9.grid(row=9, column=2)

    #Buttons of grid 5
    G5_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button1, 1, 5))
    G5_button1.grid(row=7, column=4)

    G5_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button2, 2, 5))
    G5_button2.grid(row=7, column=5)

    G5_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button3, 3, 5))
    G5_button3.grid(row=7, column=6)

    G5_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button4, 4, 5))
    G5_button4.grid(row=8, column=4)

    G5_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button5, 5, 5))
    G5_button5.grid(row=8, column=5)

    G5_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button6, 6, 5))
    G5_button6.grid(row=8, column=6)

    G5_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button7, 7, 5))
    G5_button7.grid(row=9, column=4)

    G5_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button8, 8, 5))
    G5_button8.grid(row=9, column=5)

    G5_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button9, 9, 5))
    G5_button9.grid(row=9, column=6)

    #Buttons of grid 6
    G6_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button1, 1, 6))
    G6_button1.grid(row=7, column=8)

    G6_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button2, 2, 6))
    G6_button2.grid(row=7, column=9)

    G6_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button3, 3, 6))
    G6_button3.grid(row=7, column=10)

    G6_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button4, 4, 6))
    G6_button4.grid(row=8, column=8)

    G6_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button5, 5, 6))
    G6_button5.grid(row=8, column=9)

    G6_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button6, 6, 6))
    G6_button6.grid(row=8, column=10)

    G6_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button7, 7, 6))
    G6_button7.grid(row=9, column=8)

    G6_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button8, 8, 6))
    G6_button8.grid(row=9, column=9)

    G6_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button9, 9, 6))
    G6_button9.grid(row=9, column=10)

    #Buttons of Grid 7
    G7_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button1, 1, 7))
    G7_button1.grid(row=11, column=0)

    G7_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button2, 2, 7))
    G7_button2.grid(row=11, column=1)

    G7_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button3, 3, 7))
    G7_button3.grid(row=11, column=2)

    G7_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button4, 4, 7))
    G7_button4.grid(row=12, column=0)

    G7_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button5, 5, 7))
    G7_button5.grid(row=12, column=1)

    G7_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button6, 6, 7))
    G7_button6.grid(row=12, column=2)

    G7_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button7, 7, 7))
    G7_button7.grid(row=13, column=0)

    G7_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button8, 8, 7))
    G7_button8.grid(row=13, column=1)

    G7_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button9, 9, 7))
    G7_button9.grid(row=13, column=2)

    #Buttons of grid 8
    G8_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button1, 1, 8))
    G8_button1.grid(row=11, column=4)

    G8_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button2, 2, 8))
    G8_button2.grid(row=11, column=5)

    G8_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button3, 3, 8))
    G8_button3.grid(row=11, column=6)

    G8_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button4, 4, 8))
    G8_button4.grid(row=12, column=4)

    G8_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button5, 5, 8))
    G8_button5.grid(row=12, column=5)

    G8_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button6, 6, 8))
    G8_button6.grid(row=12, column=6)

    G8_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button7, 7, 8))
    G8_button7.grid(row=13, column=4)

    G8_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button8, 8, 8))
    G8_button8.grid(row=13, column=5)

    G8_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button9, 9, 8))
    G8_button9.grid(row=13, column=6)

    #Buttons of grid 9
    G9_button1 = Button(tk, text=" ", font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button1, 1, 9))
    G9_button1.grid(row=11, column=8)

    G9_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button2, 2, 9))
    G9_button2.grid(row=11, column=9)

    G9_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button3, 3, 9))
    G9_button3.grid(row=11, column=10)

    G9_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button4, 4, 9))
    G9_button4.grid(row=12, column=8)

    G9_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button5, 5, 9))
    G9_button5.grid(row=12, column=9)

    G9_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button6, 6, 9))
    G9_button6.grid(row=12, column=10)

    G9_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button7, 7, 9))
    G9_button7.grid(row=13, column=8)

    G9_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button8, 8, 9))
    G9_button8.grid(row=13, column=9)

    G9_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button9, 9, 9))
    G9_button9.grid(row=13, column=10)

    # Vertical gaps
    gap(3, 3)
    gap(7, 7)

    # Horizontal gaps
    gap(6, 6)
    gap(10, 6)

    global grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9
    grid1 = [G1_button1, G1_button2, G1_button3, G1_button4, G1_button5, G1_button6, G1_button7, G1_button8, G1_button9]
    grid2 = [G2_button1, G2_button2, G2_button3, G2_button4, G2_button5, G2_button6, G2_button7, G2_button8, G2_button9]
    grid3 = [G3_button1, G3_button2, G3_button3, G3_button4, G3_button5, G3_button6, G3_button7, G3_button8, G3_button9]
    grid4 = [G4_button1, G4_button2, G4_button3, G4_button4, G4_button5, G4_button6, G4_button7, G4_button8, G4_button9]
    grid5 = [G5_button1, G5_button2, G5_button3, G5_button4, G5_button5, G5_button6, G5_button7, G5_button8, G5_button9]
    grid6 = [G6_button1, G6_button2, G6_button3, G6_button4, G6_button5, G6_button6, G6_button7, G6_button8, G6_button9]
    grid7 = [G7_button1, G7_button2, G7_button3, G7_button4, G7_button5, G7_button6, G7_button7, G7_button8, G7_button9]
    grid8 = [G8_button1, G8_button2, G8_button3, G8_button4, G8_button5, G8_button6, G8_button7, G8_button8, G8_button9]
    grid9 = [G9_button1, G9_button2, G9_button3, G9_button4, G9_button5, G9_button6, G9_button7, G9_button8, G9_button9]

def nextGrid(next_Grid, this_grid):
    if next_Grid == 1:
        for ding in grid1:
            ding["bg"] = "lightgray"
        if this_grid != 1:
            thisGrid(this_grid)
    elif next_Grid == 2:
        for ding in grid2:
            ding["bg"] = "lightgray"
        if this_grid != 2:
            thisGrid(this_grid)
    elif next_Grid == 3:
        for ding in grid3:
            ding["bg"] = "lightgray"
        if this_grid != 3:
            thisGrid(this_grid)
    elif next_Grid == 4:
        for ding in grid4:
            ding["bg"] = "lightgray"
        if this_grid != 4:
            thisGrid(this_grid)
    elif next_Grid == 5:
        for ding in grid5:
            ding["bg"] = "lightgray"
        if this_grid != 5:
            thisGrid(this_grid)
    elif next_Grid == 6:
        for ding in grid6:
            ding["bg"] = "lightgray"
        if this_grid != 6:
            thisGrid(this_grid)
    elif next_Grid == 7:
        for ding in grid7:
            ding["bg"] = "lightgray"
        if this_grid != 7:
            thisGrid(this_grid)
    elif next_Grid == 8:
        for ding in grid8:
            ding["bg"] = "lightgray"
        if this_grid != 8:
            thisGrid(this_grid)
    else:
        for ding in grid9:
            ding["bg"] = "lightgray"
        if this_grid != 9:
            thisGrid(this_grid)

def thisGrid(Grid):
    if Grid == 1:
        for ding in grid1:
            ding["bg"] = "gray"
    elif Grid == 2:
        for ding in grid2:
            ding["bg"] = "gray"
    elif Grid == 3:
        for ding in grid3:
            ding["bg"] = "gray"
    elif Grid == 4:
        for ding in grid4:
            ding["bg"] = "gray"
    elif Grid == 5:
        for ding in grid5:
            ding["bg"] = "gray"
    elif Grid == 6:
        for ding in grid6:
            ding["bg"] = "gray"
    elif Grid == 7:
        for ding in grid7:
            ding["bg"] = "gray"
    elif Grid == 8:
        for ding in grid8:
            ding["bg"] = "gray"
    else:
        for ding in grid9:
            ding["bg"] = "gray"

def PVE():
    global p2
    p2 = "Ai"

    label_p = Label(tk, text="Player:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
    label_p.grid(row=1, column=0)

    player_name = Entry(tk, textvariable=p1, bd=5)
    player_name.grid(row=1, column=1, columnspan=8)

    start_knop = Button(tk, text="Start Game", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2", command=lambda: (destroy_buttons([label_p, player_name, start_knop, terug_knop]), make_Grids()))
    start_knop.grid(row=3, column=0)

    terug_knop = Button(tk, text="Terug", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2", command=lambda: (destroy_buttons([label_p, player_name, start_knop, terug_knop]), startPagina()))
    terug_knop.grid(row=3, column=1)

def PVP():
    label_p1 = Label(tk, text="Player 1:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
    label_p1.grid(row=1, column=0)
    label_p2 = Label(tk, text="Player 2:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
    label_p2.grid(row=2, column=0)

    player1_name = Entry(tk, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=8)

    player2_name = Entry(tk, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=8)

    start_knop = Button(tk, text="Start Game", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2",
                        command=lambda: (destroy_buttons([label_p1, player1_name, label_p2, player2_name, start_knop, terug_knop]), make_Grids()))
    start_knop.grid(row=3, column=0)

    terug_knop = Button(tk, text="Terug", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2",
                        command=lambda: (
                        destroy_buttons([label_p1, player1_name, label_p2, player2_name, start_knop, terug_knop]), startPagina()))
    terug_knop.grid(row=3, column=1)

def hyperlink(url):
    webbrowser.open_new(url)

def Regels():
    regels = Label(tk, text="*Elk klein 3x3 bord word verwezen als klein bord en het grote 3x3 bord word verwezen als een groot bord*\n"
                             "\n- Het spel begint met Player 1 die één van de 81 lege vakjes kiest om daar zijn X te zetten.\n "
                             "Deze zet stuurt de tegenstander naar de relatieve locatie."
                             "\n- Als een zet gespeeld word dat er voor zorgt dat het kleine bord word gewonnen,"
                             "\n dan word het kleine bord gemarkeerd als een overwinning voor de speler op het grote bord"
                             "\n- Wanneer een klein bord is gewonnen of vol zit dan word er niet meer op dat bord gespeeld. "
                             "\nAls een speler naar zo'n bord word gestuurd dan mag die speler in elk ander bord een zet zetten."
                             "\n- Het spel eindigd als een speler het grote bord wint of als er geen legale zetten over blijven, "
                             "\nin dit geval is het dan een gelijk spel.", font='Times 15 bold', fg='black', height=11, width=80)
    regels.grid(row=1, column=0)

    link = Button(tk, text="Klik voor video uitleg", font='Times 15 bold',  fg='blue', cursor="hand2", command=lambda:hyperlink("https://www.youtube.com/watch?v=37PC0bGMiTI"))
    link.grid(row=2, column=0)

    terug_knop = Button(tk, text="Terug", font='Times 10 bold', bg='gray', fg='white', cursor="hand2",
                        command=lambda: (
                            destroy_buttons([regels, terug_knop, link]),
                            startPagina()))
    terug_knop.grid(row=3, column=0)

def destroy_buttons(knoppen):
    for knop in knoppen:
        knop.destroy()

def startPagina():
    PVP_button = Button(tk, text="PVP", font='Times 10 bold', bg='gray', fg='white', cursor="hand2", height=1, width=50, command=lambda: (destroy_buttons([PVP_button, PVE_button, Regels_button, tekst]), PVP()))
    PVP_button.grid(row=1, column=0)

    PVE_button = Button(tk, text="PVE", font='Times 10 bold', bg='gray', fg='white', cursor="hand2", height=1, width=50, command=lambda: (destroy_buttons([PVE_button, PVP_button, Regels_button, tekst]), PVE()))
    PVE_button.grid(row=2, column=0)

    Regels_button = Button(tk, text="Regels", font='Times 10 bold', bg='gray', fg='white', cursor="hand2", height=1, width=50, command=lambda: (destroy_buttons([PVE_button, PVP_button, Regels_button, tekst]), Regels()))
    Regels_button.grid(row=3, column=0)

    tekst = Label(tk, text= "Welkom bij Ultimate Tic-Tac-Toe", fg='black')
    tekst.grid(row=0, column=0)

startPagina()
tk.mainloop()