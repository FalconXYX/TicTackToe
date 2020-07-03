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
square1 = 0
square2 = 0
square3 = 0
square4 = 0
square5 = 0
square6 = 0
square7 = 0
square8 = 0
square9 = 0
turn = 0
clicked1 = False
clicked2 = False
clicked3 = False
clicked4 = False
clicked5 = False
clicked6 = False
clicked7 = False
clicked8 = False
clicked9 = False

class App(tk.Tk):
    def __init__(self):
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
        global win
        player = 1
        tk.Tk.__init__(self)
        self.title("Fund Manager")
        self.geometry("780x600") #Width x Height of selfdow
        Title = tk.Label(self, text="Tic Tac Toe", fg="Black",font=("Courier", 44))
        Title.place(x=200, y=0)
        win = tk.Label(self, text="Player 1 is X    Player 2 is O", fg="Black",font=("Courier", 24))
        win.place(x=110, y=60)
        self.lines()


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
        place2 = tk.Button(self, text="", command=self.game2)
        place3 = tk.Button(self, text="", command=self.game3)
        place4 = tk.Button(self, text="", command=self.game4)
        place5 = tk.Button(self, text="", command=self.game5)
        place6 = tk.Button(self, text="", command=self.game6)
        place7 = tk.Button(self, text="", command=self.game7)
        place8 = tk.Button(self, text="", command=self.game8)
        place9 = tk.Button(self, text="", command=self.game9)
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
        global square1
        global square2
        global square3
        global square4
        global square5
        global square6
        global square7
        global square8
        global square9
        global turn
        global clicked1
        global clicked2
        global clicked3
        global clicked4
        global clicked5
        global clicked6
        global clicked7
        global clicked8
        global clicked9
        print(turn)
        row1 = square1 + square2 + square3
        row2 = square4 + square5 + square6
        row3 = square7 + square8 + square9
        c1 = square1 + square4 + square7
        c2 = square2 + square5 + square8
        c3 = square3 + square6 + square9
        d1 = square1 + square5 + square9
        d2 = square7 + square5 + square3
        if row1 == 3 or row2 == 3 or row3 == 3 or c1 == 3 or c2 == 3 or c3 == 3 or d1 == 3 or d2 == 3:
            win.configure(text="Player 1 Wins")
            win.place(x=260, y=60)
            clicked1 = True
            clicked2 = True
            clicked3 = True
            clicked4 = True
            clicked5 = True
            clicked6 = True
            clicked7 = True
            clicked8 = True
            clicked9 = True
        if row1 == 15 or row2 == 15 or row3 == 15 or c1 == 15 or c2 == 15 or c3 == 15 or d1 == 15 or d2 == 15:
            win.configure(text="Player 2 Wins")
            win.place(x=260, y=60)
            clicked1 = True
            clicked2 = True
            clicked3 = True
            clicked4 = True
            clicked5 = True
            clicked6 = True
            clicked7 = True
            clicked8 = True
            clicked9 = True
        else:
            turn += 1
        if turn == 9:
            win.configure(text="Its a Tie")
            win.place(x=260, y=60)



    def game1(self):
        global player
        global place1
        global square1
        global clicked1
        if clicked1 == False:
            if player == 1:
                place1.configure(text="X")
                square1 = 1
                player = 2
            elif player == 2:
                place1.configure(text="O")
                square1 = 5
                player = 1
            clicked1 = True
            self.endgame()
    def game2(self):
        global player
        global square2
        global place2
        global clicked2
        if clicked2 == False:
            if player == 1:
                place2.configure(text="X")
                square2 = 1
                player = 2
            elif player == 2:
                place2.configure(text="O")
                square2 = 5
                player = 1
            clicked2 = True
            self.endgame()
    def game3(self):
        global player
        global square3
        global place3
        global clicked3
        if clicked3 == False:
            if player == 1:
                place3.configure(text="X")
                square3 = 1
                player = 2
            elif player == 2:
                place3.configure(text="O")
                square3 = 5
                player = 1
            clicked3 = True
            self.endgame()
    def game4(self):
        global player
        global place4
        global square4
        global clicked4
        if clicked4 == False:
            if player == 1:
                place4.configure(text="X")
                square4 = 1
                player = 2
            elif player == 2:
                place4.configure(text="O")
                square4 = 5
                player = 1
            clicked4 = True
            self.endgame()
    def game5(self):
        global place5
        global player
        global square5
        global clicked5
        if clicked5 == False:
            if player == 1:
                place5.configure(text="X")
                square5 = 1
                player = 2
            elif player == 2:
                place5.configure(text="O")
                square5 = 5
                player = 1
            clicked5 = True
            self.endgame()
    def game6(self):
        global player
        global place6
        global square6
        global clicked6
        if clicked6 == False:
            if player == 1:
                place6.configure(text="X")
                square6 = 1
                player = 2
            elif player == 2:
                place6.configure(text="O")
                square6 = 5
                player = 1
            clicked6 = True
            self.endgame()
    def game7(self):
        global player
        global place7
        global square7
        global clicked7
        if clicked7 == False:
            if player == 1:
                place7.configure(text="X")
                square7 = 1
                player = 2
            elif player == 2:
                place7.configure(text="O")
                square7 = 5
                player = 1
            clicked7 = True
            self.endgame()
    def game8(self):
        global player
        global place8
        global square8
        global clicked8
        if clicked8 == False:
            if player == 1:
                place8.configure(text="X")
                square8 = 1
                player = 2
            elif player == 2:
                place8.configure(text="O")
                square8 = 5
                player = 1
            clicked8 = True
            self.endgame()
    def game9(self):
        global player
        global place9
        global square9
        global clicked9
        if clicked9 == False:
            if player == 1:
                place9.configure(text="X")
                square9 = 1
                player = 2
            elif player == 2:
                place9.configure(text="O")
                square9 = 5
                player = 1
            clicked9 = True
            self.endgame()



    def clear(self):
        time.sleep(0.5)
        list = self.place_slaves()
        for l in list:
            l.destroy()





w = App()
w.mainloop()
