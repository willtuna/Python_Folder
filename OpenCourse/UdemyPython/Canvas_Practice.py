#! /usr/bin/env python3

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_rectangle(20,20,100,270)
canvas.create_polygon(0,0,  5,20, 50,30, 40,15)
canvas.create_line(0,0,100,100)


root.mainloop()
