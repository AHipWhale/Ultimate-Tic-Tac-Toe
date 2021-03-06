import tkinter.messagebox

from AI import *
from Game import *
from tkinter import *
import webbrowser

tk = Tk()
tk.title("Ultimate Tic-Tac-Toe")

#Namen van spelers
p1 = StringVar()
p2 = StringVar()

singlePlayerMode = False

#Welke speler aan de beurt is
bclick = '1'

def changeMode(TrueOrFalse):
    """Veranderd de mode van het spel"""
    global singlePlayerMode
    singlePlayerMode = TrueOrFalse

def btnClick_PVP(buttons, next_Grid, thisGrid):
    """Deze functie is voor de PVP modus van het spel. De fucntie zet de X en O neer op de plek die de speler heeft gekozen.
       Vervolgens word er gecheckt of een grid winst, gelijkspel of dat je je symbol niet kan plaatsen
       want het vak is al een eerder gekozen. En word de volgende grid gehighlight"""
    global bclick, p1, p2

    #Is de knop 'leeg' en is speler 1 aan de beurt
    if buttons["text"] == " " and bclick == '1':
        buttons["text"] = "X"
        bclick = '2'

        #Heeft X de grid gewonnen
        checkForWinReturn = checkForGridWin(thisGrid, False)
        if checkForWinReturn == "X":
            wonGrid(thisGrid, "X")

        #Veranderd toegang van grids
        nextGrid(next_Grid, thisGrid)
        if checkForFullGrid(next_Grid):
            allowAcces(allGrids)

    #Is de knop 'leeg' en is speler 2 aan de beurt
    elif buttons["text"] == " " and bclick == '2':
        buttons["text"] = "O"
        bclick = '1'

        checkForWinReturn = checkForGridWin(thisGrid, False)
        if checkForWinReturn == "O":
            wonGrid(thisGrid, "O")

        nextGrid(next_Grid, thisGrid)
        if checkForFullGrid(next_Grid):
            allowAcces(allGrids)
    else:
        #Knop is niet leeg
        tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", "Button already Clicked!")

def btnClick_PVAi(buttons, next_Grid, thisGrid):
    """Deze functie is voor de PVE modus van het spel. De fucntie zet de X neer op de plek die de speler heeft gekozen.
       Vervolgens word er gecheckt of een grid winst, gelijkspel of dat je je symbol niet kan plaatsen
       want het vak is al een eerder gekozen. En word de volgende grid gehighlight. Ook word het Ai algortime opgeroepen.
       (Deze funcitie lijkt op 'btnClick_PVP'.)"""
    global bclick, p1, p2
    if buttons["text"] == " " and bclick == '1':
        buttons["text"] = "X"

        checkForWinReturn = checkForGridWin(thisGrid, False)
        if checkForWinReturn == "X":
            wonGrid(thisGrid, "X")

        greyGrid(thisGrid)
        nextGrid(play_alpha_beta(next_Grid, allGrids), next_Grid)

        if checkForGridWin(next_Grid, False) == 'O':
            wonGrid(next_Grid, 'O')
    else:
        tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", "Button already Clicked!")

def btnClick(buttons, next_Grid, thisGrid):
    """Deze functie kijkt bij elke keer als een knop word aangeklikt, in welke modus het spel zit."""
    if singlePlayerMode == True:
        btnClick_PVAi(buttons, next_Grid, thisGrid)
    else:
        btnClick_PVP(buttons, next_Grid, thisGrid)

def gap(row, column):
    """Deze functie maakt een gat tussen de grids van het spel."""
    # Dit stukje is voor de kloof tussen de grids
    label = Label(tk, height=1, width=1)
    label.grid(row=row, column=column)

def make_Grids():
    """Deze functie maakt de knoppen van het spel aan."""
    global grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, allGrids
    H = 2  # hoogte van de knoppen
    W = 4  # breedte van de knoppen
    fg = 'white' # letterkleur
    bg = 'gray' # achtergrondkleur
    font = 'Times 20 bold' # lettertype

    #Knoppen van grid 1
    G1_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button1, grid1, grid1))
    G1_button1.grid(row=3, column=0)

    G1_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button2, grid2, grid1))
    G1_button2.grid(row=3, column=1)

    G1_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button3, grid3, grid1))
    G1_button3.grid(row=3, column=2)

    G1_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button4, grid4, grid1))
    G1_button4.grid(row=4, column=0)

    G1_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button5, grid5, grid1))
    G1_button5.grid(row=4, column=1)

    G1_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button6, grid6, grid1))
    G1_button6.grid(row=4, column=2)

    G1_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button7, grid7, grid1))
    G1_button7.grid(row=5, column=0)

    G1_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button8, grid8, grid1))
    G1_button8.grid(row=5, column=1)

    G1_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G1_button9, grid9, grid1))
    G1_button9.grid(row=5, column=2)

    #Knoppen van grid 2
    G2_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button1, grid1, grid2))
    G2_button1.grid(row=3, column=4)

    G2_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button2, grid2, grid2))
    G2_button2.grid(row=3, column=5)

    G2_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button3, grid3, grid2))
    G2_button3.grid(row=3, column=6)

    G2_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button4, grid4, grid2))
    G2_button4.grid(row=4, column=4)

    G2_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button5, grid5, grid2))
    G2_button5.grid(row=4, column=5)

    G2_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button6, grid6, grid2))
    G2_button6.grid(row=4, column=6)

    G2_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button7, grid7, grid2))
    G2_button7.grid(row=5, column=4)

    G2_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button8, grid8, grid2))
    G2_button8.grid(row=5, column=5)

    G2_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G2_button9, grid9, grid2))
    G2_button9.grid(row=5, column=6)

    #Knoppen van grid 3
    G3_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button1, grid1, grid3))
    G3_button1.grid(row=3, column=8)

    G3_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button2, grid2, grid3))
    G3_button2.grid(row=3, column=9)

    G3_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button3, grid3, grid3))
    G3_button3.grid(row=3, column=10)

    G3_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button4, grid4, grid3))
    G3_button4.grid(row=4, column=8)

    G3_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button5, grid5, grid3))
    G3_button5.grid(row=4, column=9)

    G3_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button6, grid6, grid3))
    G3_button6.grid(row=4, column=10)

    G3_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button7, grid7, grid3))
    G3_button7.grid(row=5, column=8)

    G3_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button8, grid8, grid3))
    G3_button8.grid(row=5, column=9)

    G3_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G3_button9, grid9, grid3))
    G3_button9.grid(row=5, column=10)

    #Knoppen van grid 4
    G4_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button1, grid1, grid4))
    G4_button1.grid(row=7, column=0)

    G4_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button2, grid2, grid4))
    G4_button2.grid(row=7, column=1)

    G4_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button3, grid3, grid4))
    G4_button3.grid(row=7, column=2)

    G4_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button4, grid4, grid4))
    G4_button4.grid(row=8, column=0)

    G4_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button5, grid5, grid4))
    G4_button5.grid(row=8, column=1)

    G4_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button6, grid6, grid4))
    G4_button6.grid(row=8, column=2)

    G4_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button7, grid7, grid4))
    G4_button7.grid(row=9, column=0)

    G4_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button8, grid8, grid4))
    G4_button8.grid(row=9, column=1)

    G4_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G4_button9, grid9, grid4))
    G4_button9.grid(row=9, column=2)

    #Knoppen van grid 5
    G5_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button1, grid1, grid5))
    G5_button1.grid(row=7, column=4)

    G5_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button2, grid2, grid5))
    G5_button2.grid(row=7, column=5)

    G5_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button3, grid3, grid5))
    G5_button3.grid(row=7, column=6)

    G5_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button4, grid4, grid5))
    G5_button4.grid(row=8, column=4)

    G5_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button5, grid5, grid5))
    G5_button5.grid(row=8, column=5)

    G5_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button6, grid6, grid5))
    G5_button6.grid(row=8, column=6)

    G5_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button7, grid7, grid5))
    G5_button7.grid(row=9, column=4)

    G5_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button8, grid8, grid5))
    G5_button8.grid(row=9, column=5)

    G5_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G5_button9, grid9, grid5))
    G5_button9.grid(row=9, column=6)

    #Knoppen van grid 6
    G6_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button1, grid1, grid6))
    G6_button1.grid(row=7, column=8)

    G6_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button2, grid2, grid6))
    G6_button2.grid(row=7, column=9)

    G6_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button3, grid3, grid6))
    G6_button3.grid(row=7, column=10)

    G6_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button4, grid4, grid6))
    G6_button4.grid(row=8, column=8)

    G6_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button5, grid5, grid6))
    G6_button5.grid(row=8, column=9)

    G6_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button6, grid6, grid6))
    G6_button6.grid(row=8, column=10)

    G6_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button7, grid7, grid6))
    G6_button7.grid(row=9, column=8)

    G6_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button8, grid8, grid6))
    G6_button8.grid(row=9, column=9)

    G6_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G6_button9, grid9, grid6))
    G6_button9.grid(row=9, column=10)

    #Knoppen van grid 7
    G7_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button1, grid1, grid7))
    G7_button1.grid(row=11, column=0)

    G7_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button2, grid2, grid7))
    G7_button2.grid(row=11, column=1)

    G7_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button3, grid3, grid7))
    G7_button3.grid(row=11, column=2)

    G7_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button4, grid4, grid7))
    G7_button4.grid(row=12, column=0)

    G7_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button5, grid5, grid7))
    G7_button5.grid(row=12, column=1)

    G7_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button6, grid6, grid7))
    G7_button6.grid(row=12, column=2)

    G7_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button7, grid7, grid7))
    G7_button7.grid(row=13, column=0)

    G7_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button8, grid8, grid7))
    G7_button8.grid(row=13, column=1)

    G7_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G7_button9, grid9, grid7))
    G7_button9.grid(row=13, column=2)

    #Knoppen van grid 8
    G8_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button1, grid1, grid8))
    G8_button1.grid(row=11, column=4)

    G8_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button2, grid2, grid8))
    G8_button2.grid(row=11, column=5)

    G8_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button3, grid3, grid8))
    G8_button3.grid(row=11, column=6)

    G8_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button4, grid4, grid8))
    G8_button4.grid(row=12, column=4)

    G8_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button5, grid5, grid8))
    G8_button5.grid(row=12, column=5)

    G8_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button6, grid6, grid8))
    G8_button6.grid(row=12, column=6)

    G8_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button7, grid7, grid8))
    G8_button7.grid(row=13, column=4)

    G8_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button8, grid8, grid8))
    G8_button8.grid(row=13, column=5)

    G8_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G8_button9, grid9, grid8))
    G8_button9.grid(row=13, column=6)

    #Knoppen van grid 9
    G9_button1 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button1, grid1, grid9))
    G9_button1.grid(row=11, column=8)

    G9_button2 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button2, grid2, grid9))
    G9_button2.grid(row=11, column=9)

    G9_button3 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button3, grid3, grid9))
    G9_button3.grid(row=11, column=10)

    G9_button4 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button4, grid4, grid9))
    G9_button4.grid(row=12, column=8)

    G9_button5 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button5, grid5, grid9))
    G9_button5.grid(row=12, column=9)

    G9_button6 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button6, grid6, grid9))
    G9_button6.grid(row=12, column=10)

    G9_button7 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button7, grid7, grid9))
    G9_button7.grid(row=13, column=8)

    G9_button8 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button8, grid8, grid9))
    G9_button8.grid(row=13, column=9)

    G9_button9 = Button(tk, text=' ', font=font, bg=bg, fg=fg, height=H, width=W, command=lambda: btnClick(G9_button9, grid9, grid9))
    G9_button9.grid(row=13, column=10)

    # Verticale kloven
    gap(3, 3)
    gap(7, 7)

    # Horizontale kloven
    gap(6, 6)
    gap(10, 6)

    #Lijsten met knoppen die bij de grid horen
    grid1 = [G1_button1, G1_button2, G1_button3, G1_button4, G1_button5, G1_button6, G1_button7, G1_button8, G1_button9]
    grid2 = [G2_button1, G2_button2, G2_button3, G2_button4, G2_button5, G2_button6, G2_button7, G2_button8, G2_button9]
    grid3 = [G3_button1, G3_button2, G3_button3, G3_button4, G3_button5, G3_button6, G3_button7, G3_button8, G3_button9]
    grid4 = [G4_button1, G4_button2, G4_button3, G4_button4, G4_button5, G4_button6, G4_button7, G4_button8, G4_button9]
    grid5 = [G5_button1, G5_button2, G5_button3, G5_button4, G5_button5, G5_button6, G5_button7, G5_button8, G5_button9]
    grid6 = [G6_button1, G6_button2, G6_button3, G6_button4, G6_button5, G6_button6, G6_button7, G6_button8, G6_button9]
    grid7 = [G7_button1, G7_button2, G7_button3, G7_button4, G7_button5, G7_button6, G7_button7, G7_button8, G7_button9]
    grid8 = [G8_button1, G8_button2, G8_button3, G8_button4, G8_button5, G8_button6, G8_button7, G8_button8, G8_button9]
    grid9 = [G9_button1, G9_button2, G9_button3, G9_button4, G9_button5, G9_button6, G9_button7, G9_button8, G9_button9]
    allGrids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9]

def nextGrid(next_Grid, this_grid):
    """Deze functie highlight de grid waar gespeelt in moet worden.
       Roept een functie aan die de acces van de knoppen veranderd. Voor de Ai kijkt deze fucntie ook of de grid volzit."""
    if singlePlayerMode == False:
        #Veranderd kleur van knoppen
        for vak in next_Grid:
            vak["bg"] = "lightgray"
        if this_grid != next_Grid:
            greyGrid(this_grid)
        #Veranderd de toegang van de grids
        changeAcces(next_Grid, allGrids)
    else:
        next_Grid = getNextGrid(next_Grid, allGrids)
        for vak in next_Grid:
            vak["bg"] = "lightgray"
        if this_grid != next_Grid:
            greyGrid(this_grid)
        if checkForFullGrid(next_Grid):
            allowAcces(allGrids)
        else:
            changeAcces(next_Grid, allGrids)

def greyGrid(Grid):
    """Deze functie maakt elk vak in de meegegeven grid de kleur grijs."""
    for vak in Grid:
        vak["bg"] = "gray"

def PVE():
    """Deze functie word aangeroepen na het aanklikken van de 'PVE' knop op de startpagina.
       De functie laat je de naam van de speler invullen en voegt een start en terug knop toe om
       terug te gaan naar de startpagina of het spel te starten."""
    global p1, p2
    p2 = "Ai"

    #label voor speler
    label_p = Label(tk, text="Player:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
    label_p.grid(row=1, column=0)

    #Invul plek voor naam
    player_name = Entry(tk, textvariable=p1, bd=5)
    player_name.grid(row=1, column=1, columnspan=8)

    #Start knop
    start_knop = Button(tk, text="Start Game", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2", command=lambda: (destroy_buttons([label_p, player_name, start_knop, terug_knop]), changeMode(True), make_Grids()))
    start_knop.grid(row=3, column=0)

    #Terug knop
    terug_knop = Button(tk, text="Terug", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2", command=lambda: (destroy_buttons([label_p, player_name, start_knop, terug_knop]), startPagina()))
    terug_knop.grid(row=3, column=1)

def PVP():
    """Deze functie word aangeroepen na het aanklikken van de 'PVP' knop op de startpagina.
       De functie laat je de naam van beide spelers invullen en voegt een start en terug knop toe om
       terug te gaan naar de startpagina of het spel te starten."""
    global p1, p2

    #Lebel voor spelers
    label_p1 = Label(tk, text="Player 1:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
    label_p1.grid(row=1, column=0)
    label_p2 = Label(tk, text="Player 2:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
    label_p2.grid(row=2, column=0)

    #Invul plek voor namen
    player1_name = Entry(tk, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=8)

    player2_name = Entry(tk, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=8)

    #Start knop
    start_knop = Button(tk, text="Start Game", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2",
                        command=lambda: (destroy_buttons([label_p1, player1_name, label_p2, player2_name, start_knop, terug_knop]), changeMode(False), make_Grids()))
    start_knop.grid(row=3, column=0)

    #Terug knop
    terug_knop = Button(tk, text="Terug", font='Times 10 bold', bg='gray', fg='white', height=1, width=13, cursor="hand2",
                        command=lambda: (
                        destroy_buttons([label_p1, player1_name, label_p2, player2_name, start_knop, terug_knop]), startPagina()))
    terug_knop.grid(row=3, column=1) 

def hyperlink(url):
    """Deze functie maakt een hyperlink naar een bepaalde url aan."""
    webbrowser.open_new(url)

def Regels():
    """Deze functie is voor de pagina 'regels'. Hier word de tekst en de knoppen aangemaakt."""
    #Lebel met regels
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

    #Knop voor hyperlink
    link = Button(tk, text="Klik voor video uitleg", font='Times 15 bold',  fg='blue', cursor="hand2", command=lambda:hyperlink("https://www.youtube.com/watch?v=37PC0bGMiTI"))
    link.grid(row=2, column=0)

    #Terug knop
    terug_knop = Button(tk, text="Terug", font='Times 10 bold', bg='gray', fg='white', cursor="hand2",
                        command=lambda: (
                            destroy_buttons([regels, terug_knop, link]),
                            startPagina()))
    terug_knop.grid(row=3, column=0)

def destroy_buttons(knoppen):
    """Deze functie zorgt ervoor dat knoppen worden verwijderd. Bijvoorbeeld bij het switchen van pagina."""
    for knop in knoppen:
        knop.destroy()

def startPagina():
    """Deze functie maakt de startpagina aan met een welkom tekst en drie knoppen.
       Één voor de regels en twee om de mode van het spel te veranderen"""
    #Knop voor PVP mode
    PVP_button = Button(tk, text="PVP", font='Times 10 bold', bg='gray', fg='white', cursor="hand2", height=1, width=50, command=lambda: (destroy_buttons([PVP_button, PVE_button, Regels_button, tekst]), PVP()))
    PVP_button.grid(row=1, column=0)

    #Knop voor PVE mode
    PVE_button = Button(tk, text="PVE", font='Times 10 bold', bg='gray', fg='white', cursor="hand2", height=1, width=50, command=lambda: (destroy_buttons([PVE_button, PVP_button, Regels_button, tekst]), PVE()))
    PVE_button.grid(row=2, column=0)

    #Knop voor regels
    Regels_button = Button(tk, text="Regels", font='Times 10 bold', bg='gray', fg='white', cursor="hand2", height=1, width=50, command=lambda: (destroy_buttons([PVE_button, PVP_button, Regels_button, tekst]), Regels()))
    Regels_button.grid(row=3, column=0)

    #Welkomtekst
    tekst = Label(tk, text= "Welkom bij Ultimate Tic-Tac-Toe", fg='black')
    tekst.grid(row=0, column=0)

def wonGrid(grid, symbol):
    """Deze functie word aangeroepen als een grid gewonnen is en veranderd de tekst elk vak in die grid naar het symbool.
       Ook word hier een fucntie aangeroepen die kijkt of het hele spel is gewonnen"""
    for vak in grid:
        vak['text'] = symbol
    checkForGameWin(allGrids, grid, symbol, p1, p2)

startPagina()
tk.mainloop()