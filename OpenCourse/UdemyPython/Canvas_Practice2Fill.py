#! /usr/bin/env python3

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def createRect(x1,y1, x2,y2):
    canvas.create_rectangle(x1,y1, x2,y2, fill="blue")

def randomRects(num):
    color = ["red","blue","yellow","White"]
    random.shuffle(color)
    for i in range(0,num):
        x1 = random.randrange(150)
        y1 = random.randrange(150)
        x2 = x1 + random.randrange(150)
        y2 = y1 + random.randrange(150)
        canvas.create_rectangle(x1,y1,x2,y2, fill=color[random.randint(0,3)])




createRect(5,50,200,70)

createRect(5,5,40,200)

randomRects(300)




root.mainloop()
