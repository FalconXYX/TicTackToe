#--------------------
#Import stuff
#--------------------
import sys
import random
import tkinter as tk
import time
from tkinter import *
#--------------------
#Variable stuff
#--------------------
square = [0,0,0,0,0,0,0,0,0]

turn = 0
clicked = [False,False,False,False,False,False,False,False,False]


class App(tk.Tk):
    def __init__(self):
        global player
        global square
        global place1
        global place2
        global place3
        global place4
        global place5
        global place6
        global place7
        global place8
        global place9
        global win
        player = 1
        tk.Tk.__init__(self)
        self.title("Tic Tac Toe")
        self.geometry("780x600") #Width x Height of selfdow
        Title = tk.Label(self, text="Tic Tac Toe", fg="Black",font=("Courier", 44))
        Title.place(x=200, y=0)
        win = tk.Label(self, text="Player 1 is X    Player 2 is O", fg="Black",font=("Courier", 24))
        win.place(x=110, y=60)
        self.lines()
        print(square[2])


    def lines(self):
        global player
        global place1
        global place2
        global place3
        global place4
        global place5
        global place6
        global place7
        global place8
        global place9


        player = 1
        w = Canvas(self, width=780, height=500)
        w.place(x=0, y=100)
        w.create_line(225, 180, 525, 180)
        w.create_line(225, 280, 525, 280)
        w.create_line(325, 380, 325, 80)
        w.create_line(425, 380, 425, 80)
        place1 = tk.Button(self, text="", command=self.game1)
        place2  = tk.Button(self, text="", command=self.game2)
        place3  = tk.Button(self, text="", command=self.game3)
        place4  = tk.Button(self, text="", command=self.game4)
        place5 = tk.Button(self, text="", command=self.game5)
        place6  = tk.Button(self, text="", command=self.game6)
        place7  =  tk.Button(self, text="", command=self.game7)
        place8  =  tk.Button(self, text="", command=self.game8)
        place9  =  tk.Button(self, text="", command=self.game9)

        place1.place(x=270, y=220)
        place2.place(x=370, y=220)
        place3.place(x=470, y=220)
        place4.place(x=270, y=320)
        place5.place(x=370, y=320)
        place6.place(x=470, y=320)
        place7.place(x=270, y=420)
        place8.place(x=370, y=420)
        place9.place(x=470, y=420)
    def endgame(self):
        global win
        global square
        global turn
        global clicked
        print(turn)
        row1 = square[0] + square[1] + square[2]
        row2 = square[3] + square[4] + square[5]
        row3 = square[6] + square[7] + square[8]
        c1 = square[0] + square[3] + square[6]
        c2 = square[1] + square[4] + square[7]
        c3 = square[2] + square[5] + square[8]
        d1 = square[0] + square[4] + square[8]
        d2 = square[6] + square[4] + square[2]
        if row1 == 3 or row2 == 3 or row3 == 3 or c1 == 3 or c2 == 3 or c3 == 3 or d1 == 3 or d2 == 3:
            win.configure(text="Player 1 Wins")
            win.place(x=260, y=60)
            clicked[0] = True
            clicked[1] = True
            clicked[2] = True
            clicked[3] = True
            clicked[4] = True
            clicked[5] = True
            clicked[6] = True
            clicked[7] = True
            clicked[8] = True
        if row1 == 15 or row2 == 15 or row3 == 15 or c1 == 15 or c2 == 15 or c3 == 15 or d1 == 15 or d2 == 15:
            win.configure(text="Player 2 Wins")
            win.place(x=260, y=60)
            clicked[0] = True
            clicked[1] = True
            clicked[2] = True
            clicked[3] = True
            clicked[4] = True
            clicked[5] = True
            clicked[6] = True
            clicked[7] = True
            clicked[8] = True
        else:
            turn += 1
        if turn == 9:
            win.configure(text="Its a Tie")
            win.place(x=260, y=60)



    def game1(self):
        global player
        global place
        global square
        global clicked
        if clicked[0] == False:
            if player == 1:
                place1.configure(text="X")
                square[0] = 1
                player = 2
            elif player == 2:
                place1.configure(text="O")
                square[0] = 5
                player = 1
            clicked[0] = True
            self.endgame()
    def game2(self):
        global player
        global square
        global place2
        global clicked
        if clicked[1] == False:
            if player == 1:
                place2.configure(text="X")
                square[1] = 1
                player = 2
            elif player == 2:
                place2.configure(text="O")
                square[1] = 5
                player = 1
            clicked[1] = True
            self.endgame()
    def game3(self):
        global player
        global square
        global place3
        global clicked
        if clicked[2] == False:
            if player == 1:
                place3.configure(text="X")
                square[2] = 1
                player = 2
            elif player == 2:
                place3.configure(text="O")
                square[2] = 5
                player = 1
            clicked[2] = True
            self.endgame()
    def game4(self):
        global player
        global place4
        global square
        global clicked
        if clicked[3] == False:
            if player == 1:
                place4.configure(text="X")
                square[3] = 1
                player = 2
            elif player == 2:
                place4.configure(text="O")
                square[3] = 5
                player = 1
            clicked[3] = True
            self.endgame()
    def game5(self):
        global place5
        global player
        global square
        global clicked
        if clicked[4] == False:
            if player == 1:
                place5.configure(text="X")
                square[4] = 1
                player = 2
            elif player == 2:
                place5.configure(text="O")
                square[4] = 5
                player = 1
            clicked[4] = True
            self.endgame()
    def game6(self):
        global player
        global place6
        global square
        global clicked
        if clicked[5] == False:
            if player == 1:
                place6.configure(text="X")
                square[5] = 1
                player = 2
            elif player == 2:
                place6.configure(text="O")
                square[5] = 5
                player = 1
            clicked[5] = True
            self.endgame()
    def game7(self):
        global player
        global place7
        global square
        global clicked
        if clicked[6] == False:
            if player == 1:
                place7.configure(text="X")
                square[6] = 1
                player = 2
            elif player == 2:
                place7.configure(text="O")
                square[6] = 5
                player = 1
            clicked[6] = True
            self.endgame()
    def game8(self):
        global player
        global place8
        global square
        global clicked
        if clicked[7] == False:
            if player == 1:
                place8.configure(text="X")
                square[7] = 1
                player = 2
            elif player == 2:
                place8.configure(text="O")
                square[7] = 5
                player = 1
            clicked[7] = True
            self.endgame()
    def game9(self):
        global player
        global place9
        global square
        global clicked
        if clicked[8] == False:
            if player == 1:
                place9.configure(text="X")
                square[8] = 1
                player = 2
            elif player == 2:
                place9.configure(text="O")
                square[8] = 5
                player = 1
            clicked[8] = True
            self.endgame()

    def clear(self):
        time.sleep(0.5)
        list = self.place_slaves()
        for l in list:
            l.destroy()
w = App()
w.mainloop()
