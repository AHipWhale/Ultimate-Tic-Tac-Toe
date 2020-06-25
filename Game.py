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

volleGrids = 0

def checkForGridWin(grid, checkforAi):
    """Deze functie kijkt of een bepaalde grid is gewonnen door een spele
       of roept een fuctie op die kijkt of het gelijkspel is en
       returnt het symbool van de winnaar of ' ' als het gelijk spel is."""
    #Checken of X heeft gewonnen
    if (grid[0]['text'] == 'X' and grid[1]['text'] == 'X' and grid[2]['text'] == 'X' or
          grid[3]['text'] == 'X' and grid[4]['text'] == 'X' and grid[5]['text'] == 'X' or
          grid[6]['text'] == 'X' and grid[7]['text'] == 'X' and grid[8]['text'] == 'X' or
          grid[0]['text'] == 'X' and grid[3]['text'] == 'X' and grid[6]['text'] == 'X' or
          grid[1]['text'] == 'X' and grid[4]['text'] == 'X' and grid[7]['text'] == 'X' or
          grid[2]['text'] == 'X' and grid[5]['text'] == 'X' and grid[8]['text'] == 'X' or
          grid[0]['text'] == 'X' and grid[4]['text'] == 'X' and grid[8]['text'] == 'X' or
          grid[2]['text'] == 'X' and grid[4]['text'] == 'X' and grid[6]['text'] == 'X'):
        return "X"
    #Checken of O heeft gewonnen
    elif (grid[0]['text'] == 'O' and grid[1]['text'] == 'O' and grid[2]['text'] == 'O' or
          grid[3]['text'] == 'O' and grid[4]['text'] == 'O' and grid[5]['text'] == 'O' or
          grid[6]['text'] == 'O' and grid[7]['text'] == 'O' and grid[8]['text'] == 'O' or
          grid[0]['text'] == 'O' and grid[3]['text'] == 'O' and grid[6]['text'] == 'O' or
          grid[1]['text'] == 'O' and grid[4]['text'] == 'O' and grid[7]['text'] == 'O' or
          grid[2]['text'] == 'O' and grid[5]['text'] == 'O' and grid[8]['text'] == 'O' or
          grid[0]['text'] == 'O' and grid[4]['text'] == 'O' and grid[8]['text'] == 'O' or
          grid[2]['text'] == 'O' and grid[4]['text'] == 'O' and grid[6]['text'] == 'O'):
        return"O"
    #Checken of het gelijk spel is geworden
    if checkForTie(grid, checkforAi):
        return ' '

def checkForTie(grid, forAi):
    """Deze functie kijkt of bij een grid gelijk is gespeeld en als forAi
       false is dan veranderd de tekst van elk vak van de grid in 'Tie'.
       Ook wordt bij gelijkspel True gereturnt en anders False."""
    volleVakken = 0
    #Aantal volle vlakken tellen
    for vak in grid:
        if vak['text'] == 'O' or vak['text'] == 'X':
            volleVakken+=1
    if volleVakken == 9:
        if forAi == False:
            #De text van elk vak in de grid veranderen naar 'Tie'
            for vak in grid:
                vak['text'] = "Tie"
        return True
    else:
        return False

def denyAcces(allGrids):
    """Deze functie zorgt ervoor dat de knoppen van alle grids worden uitgezet."""
    for grid in allGrids:
        #veranderd de 'state' van elke knop
        for vak in grid:
            vak["state"] = DISABLED

def allowAcces(allGrids):
    """Deze functie zorgt ervoor dat de knoppen van alle grids worden aangezet en de kleur grijs krijgen.
       Deze funcie word aangeroepen als een speler een vrije keus krijgt."""
    for grid in allGrids:
        #Veranderd de 'state' van elke knop en veranderd de kleur
        for vak in grid:
            vak["state"] = NORMAL
            vak["bg"] = "gray"

def changeAcces(Grid, allGrids):
    """Deze fuctie zorgt ervoor dat de knoppen van één grid maar aan staan."""
    #Alle toegang word geweigerd
    denyAcces(allGrids)

    #De toegang van een grid word toegestaan
    for vak in Grid:
        vak["state"] = NORMAL

def checkForFullGrid(Grid):
    """Deze functie kijkt of een grid vol zit en returnt True als dat zo is."""
    full = set()
    #Zet de text van elk vak in een set
    for vak in Grid:
        full.add(vak["text"])

    #Kijkt of de set uit 1 variable bestaat en dat niet ' ' is
    if len(full) == 1 and full != {' '}:
        return True

def defineGrid(allGrids, grid, symbol):
    """Deze functie houdt bij welke grids zijn gewonnen door welke speler.
       Deze functie word gebruikt bij de 'checkForGameWin' definitie"""
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
    """Deze functie kijkt of het hele spel is gewonnen of gelijk is gespeeld
       en zorgt ervoor dat je een bericht krijgt met de uitkomst + de naam van de winnaar als die er is."""
    global volleGrids
    #Definieert de inhoud van alle grids
    defineGrid(allGrids, grid, symbol)

    #Heeft X gewonnen
    if (grid1 == 'X' and grid2 == 'X' and grid3 == 'X' or
            grid4 == 'X' and grid5 == 'X' and grid6 == 'X' or
            grid7 == 'X' and grid8 == 'X' and grid9 == 'X' or
            grid1 == 'X' and grid4 == 'X' and grid7 == 'X' or
            grid2 == 'X' and grid5 == 'X' and grid8 == 'X' or
            grid3 == 'X' and grid6 == 'X' and grid9 == 'X' or
            grid1 == 'X' and grid5 == 'X' and grid9 == 'X' or
            grid3 == 'X' and grid5 == 'X' and grid7 == 'X'):
        tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", player1.get() + " heeft gewonnen!")

    #Is het gelijkspel
    elif volleGrids == 9:
        tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", "Het is een gelijkspel!")

    #Heeft O gewonnen
    elif (grid1 == 'O' and grid2 == 'O' and grid3 == 'O' or
            grid4 == 'O' and grid5 == 'O' and grid6 == 'O' or
            grid7 == 'O' and grid8 == 'O' and grid9 == 'O' or
            grid1 == 'O' and grid4 == 'O' and grid7 == 'O' or
            grid2 == 'O' and grid5 == 'O' and grid8 == 'O' or
            grid3 == 'O' and grid6 == 'O' and grid9 == 'O' or
            grid1 == 'O' and grid5 == 'O' and grid9 == 'O' or
            grid3 == 'O' and grid5 == 'O' and grid7 == 'O'):
        if type(player2) == tkinter.StringVar:
            tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", player2.get() + " heeft gewonnen!")
        else:
            tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", player2 + " heeft gewonnen!")
    else:
        volleGrids += 1