from tkinter import *
import tkinter.messagebox
import webbrowser

tk = Tk()
tk.title("Ultimate Tic-Tac-Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

bclick = True
flag = 0

def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        flag += 1
    else:
        tkinter.messagebox.showinfo("Ultimate Tic-Tac-Toe", "Button already Clicked!")

buttons = StringVar()

H = 2 #height of the buttons
W = 4 #width of the buttons

def gap(row, column):
    # This bit is for the gap between grids
    label = Label(tk, height=1, width=1)
    label.grid(row=row, column=column)

def Grid1():
    #Buttons of Grid 1
    G1_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button1))
    G1_button1.grid(row=3, column=0)

    G1_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button2))
    G1_button2.grid(row=3, column=1)

    G1_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button3))
    G1_button3.grid(row=3, column=2)

    G1_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button4))
    G1_button4.grid(row=4, column=0)

    G1_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button5))
    G1_button5.grid(row=4, column=1)

    G1_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button6))
    G1_button6.grid(row=4, column=2)

    G1_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button7))
    G1_button7.grid(row=5, column=0)

    G1_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button8))
    G1_button8.grid(row=5, column=1)

    G1_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G1_button9))
    G1_button9.grid(row=5, column=2)

def Grid2():
    #Buttons of grid 2
    G2_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button1))
    G2_button1.grid(row=3, column=4)

    G2_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button2))
    G2_button2.grid(row=3, column=5)

    G2_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button3))
    G2_button3.grid(row=3, column=6)

    G2_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button4))
    G2_button4.grid(row=4, column=4)

    G2_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button5))
    G2_button5.grid(row=4, column=5)

    G2_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button6))
    G2_button6.grid(row=4, column=6)

    G2_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button7))
    G2_button7.grid(row=5, column=4)

    G2_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button8))
    G2_button8.grid(row=5, column=5)

    G2_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G2_button9))
    G2_button9.grid(row=5, column=6)

def Grid3():
    #Buttons of grid 3
    G3_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button1))
    G3_button1.grid(row=3, column=8)

    G3_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button2))
    G3_button2.grid(row=3, column=9)

    G3_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button3))
    G3_button3.grid(row=3, column=10)

    G3_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button4))
    G3_button4.grid(row=4, column=8)

    G3_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button5))
    G3_button5.grid(row=4, column=9)

    G3_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button6))
    G3_button6.grid(row=4, column=10)

    G3_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button7))
    G3_button7.grid(row=5, column=8)

    G3_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button8))
    G3_button8.grid(row=5, column=9)

    G3_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G3_button9))
    G3_button9.grid(row=5, column=10)

def Grid4():
    #Buttons of Grid 4
    G4_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button1))
    G4_button1.grid(row=7, column=0)

    G4_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button2))
    G4_button2.grid(row=7, column=1)

    G4_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button3))
    G4_button3.grid(row=7, column=2)

    G4_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button4))
    G4_button4.grid(row=8, column=0)

    G4_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button5))
    G4_button5.grid(row=8, column=1)

    G4_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button6))
    G4_button6.grid(row=8, column=2)

    G4_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button7))
    G4_button7.grid(row=9, column=0)

    G4_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button8))
    G4_button8.grid(row=9, column=1)

    G4_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G4_button9))
    G4_button9.grid(row=9, column=2)

def Grid5():
    #Buttons of grid 5
    G5_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button1))
    G5_button1.grid(row=7, column=4)

    G5_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button2))
    G5_button2.grid(row=7, column=5)

    G5_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button3))
    G5_button3.grid(row=7, column=6)

    G5_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button4))
    G5_button4.grid(row=8, column=4)

    G5_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button5))
    G5_button5.grid(row=8, column=5)

    G5_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button6))
    G5_button6.grid(row=8, column=6)

    G5_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button7))
    G5_button7.grid(row=9, column=4)

    G5_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button8))
    G5_button8.grid(row=9, column=5)

    G5_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G5_button9))
    G5_button9.grid(row=9, column=6)

def Grid6():
    #Buttons of grid 6
    G6_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button1))
    G6_button1.grid(row=7, column=8)

    G6_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button2))
    G6_button2.grid(row=7, column=9)

    G6_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button3))
    G6_button3.grid(row=7, column=10)

    G6_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button4))
    G6_button4.grid(row=8, column=8)

    G6_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button5))
    G6_button5.grid(row=8, column=9)

    G6_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button6))
    G6_button6.grid(row=8, column=10)

    G6_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button7))
    G6_button7.grid(row=9, column=8)

    G6_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button8))
    G6_button8.grid(row=9, column=9)

    G6_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G6_button9))
    G6_button9.grid(row=9, column=10)

def Grid7():
    #Buttons of Grid 7
    G7_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button1))
    G7_button1.grid(row=11, column=0)

    G7_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button2))
    G7_button2.grid(row=11, column=1)

    G7_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button3))
    G7_button3.grid(row=11, column=2)

    G7_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button4))
    G7_button4.grid(row=12, column=0)

    G7_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button5))
    G7_button5.grid(row=12, column=1)

    G7_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button6))
    G7_button6.grid(row=12, column=2)

    G7_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button7))
    G7_button7.grid(row=13, column=0)

    G7_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button8))
    G7_button8.grid(row=13, column=1)

    G7_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G7_button9))
    G7_button9.grid(row=13, column=2)

def Grid8():
    #Buttons of grid 8
    G8_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button1))
    G8_button1.grid(row=11, column=4)

    G8_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button2))
    G8_button2.grid(row=11, column=5)

    G8_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button3))
    G8_button3.grid(row=11, column=6)

    G8_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button4))
    G8_button4.grid(row=12, column=4)

    G8_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button5))
    G8_button5.grid(row=12, column=5)

    G8_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button6))
    G8_button6.grid(row=12, column=6)

    G8_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button7))
    G8_button7.grid(row=13, column=4)

    G8_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button8))
    G8_button8.grid(row=13, column=5)

    G8_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G8_button9))
    G8_button9.grid(row=13, column=6)

def Grid9():
    #Buttons of grid 9
    G9_button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button1))
    G9_button1.grid(row=11, column=8)

    G9_button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button2))
    G9_button2.grid(row=11, column=9)

    G9_button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button3))
    G9_button3.grid(row=11, column=10)

    G9_button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button4))
    G9_button4.grid(row=12, column=8)

    G9_button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button5))
    G9_button5.grid(row=12, column=9)

    G9_button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button6))
    G9_button6.grid(row=12, column=10)

    G9_button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button7))
    G9_button7.grid(row=13, column=8)

    G9_button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button8))
    G9_button8.grid(row=13, column=9)

    G9_button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=H, width=W, command=lambda: btnClick(G9_button9))
    G9_button9.grid(row=13, column=10)

def PVE():
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
    player2_name = Entry(tk, textvariable=p1, bd=5)
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

def make_Grids():
    Grid1()
    Grid2()
    Grid3()
    Grid4()
    Grid5()
    Grid6()
    Grid7()
    Grid8()
    Grid9()

    # Vertical gaps
    gap(3, 3)
    gap(7, 7)

    # Horizontal gaps
    gap(6, 6)
    gap(10, 6)

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