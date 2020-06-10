from tkinter import *
import tkinter.messagebox
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

make_Grids()

#Vertical gaps
gap(3, 3)
gap(7, 7)

#Horizontal gaps
gap(6, 6)
gap(10, 6)

tk.mainloop()