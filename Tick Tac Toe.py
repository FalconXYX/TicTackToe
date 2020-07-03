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

        tk.Tk.__init__(self)
        self.title("Fund Manager")
        self.geometry("780x600") #Width x Height of selfdow
        Title = tk.Label(self, text="Tic Tac Toe", fg="Black",font=("Courier", 44))
        Title.place(x=200, y=0)
        self.lines()

    def lines(self):
        w = Canvas(self, width=780, height=500)
        w.place(x=0, y=100)
        w.create_line(225, 180, 525, 180)
        w.create_line(225, 280, 525, 280)
        w.create_line(325, 380, 325, 80)
        w.create_line(425, 380, 425, 80)




    def clear(self):
        time.sleep(0.5)
        list = self.place_slaves()
        for l in list:
            l.destroy()





w = App()
w.mainloop()
