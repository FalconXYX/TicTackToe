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
square3 = 3
square4 = 0
square5 = 0
square6 = 0
square7 = 0
square8 = 0
square9 = 0

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
        player = 1
        tk.Tk.__init__(self)
        self.title("Fund Manager")
        self.geometry("780x600") #Width x Height of selfdow
        Title = tk.Label(self, text="Tic Tac Toe", fg="Black",font=("Courier", 44))
        Title.place(x=200, y=0)
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


    def game1(self):
        global player
        global place1
        global square1
        if player == 1:
            place1.configure(text="X")
            square1 = 1
            player = 2
        elif player == 2:
            place1.configure(text="O")
            square1 = 3
            player = 1
    def game2(self):
        global player
        global square2
        global place2
        if player == 1:
            place2.configure(text="X")
            square2 = 1
            player = 2
        elif player == 2:
            place2.configure(text="O")
            square2 = 3
            player = 1
    def game3(self):
        global player
        global square3
        global place3
        if player == 1:
            place3.configure(text="X")
            square3 = 1
            player = 2
        elif player == 2:
            place3.configure(text="O")
            square3 = 3
            player = 1
    def game4(self):
        global player
        global place4
        global square4
        if player == 1:
            place4.configure(text="X")
            square4 = 1
            player = 2
        elif player == 2:
            place4.configure(text="O")
            square4 = 3
            player = 1
    def game5(self):
        global place5
        global player
        global square5
        if player == 1:
            place5.configure(text="X")
            square5 = 1
            player = 2
        elif player == 2:
            place5.configure(text="O")
            square5 = 3
            player = 1
    def game6(self):
        global player
        global place6
        global square6
        if player == 1:
            place6.configure(text="X")
            square6 = 1
            player = 2
        elif player == 2:
            place6.configure(text="O")
            square6 = 3
            player = 1
    def game7(self):
        global player
        global place7
        global square7
        if player == 1:
            place7.configure(text="X")
            square7 = 1
            player = 2
        elif player == 2:
            place7.configure(text="O")
            square7 = 3
            player = 1
    def game8(self):
        global player
        global place8
        global square8
        if player == 1:
            place8.configure(text="X")
            square8 = 1
            player = 2
        elif player == 2:
            place8.configure(text="O")
            square8 = 3
            player = 1
    def game9(self):
        global player
        global place9
        global square9
        if player == 1:
            place9.configure(text="X")
            square9 = 3
            player = 2
        if player == 2:
            place9.configure(text="O")
            square9 = 3
            player = 1










    def clear(self):
        time.sleep(0.5)
        list = self.place_slaves()
        for l in list:
            l.destroy()





w = App()
w.mainloop()
