#! /usr/bin/env python3

from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width=500,height=500)
canvas.pack()

canvas.create_polygon(10,10, 10,60, 50,30)

for i in range(0,60):
    # move the object on the screen by the specific amout
    canvas.move(1,5,10) 
    #       first object, move 5 pixel in x, 10 pixel in y
    root.update()
    time.sleep(0.1)

root.mainloop()

