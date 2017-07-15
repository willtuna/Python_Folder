#! /usr/bin/env python3

from tkinter import *

root = Tk()

def leftClick(event):
    print("Left")

def RightClick(event):
    print("Right")

def Scroll(event):
    print("Scroll")

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

'''button1 = Button(root, text="Click Me")
button1.bind("<Button-1>", printName)
# <Button-1> mean left button of mouse is clicked
button1.grid(columnspan=2)
'''
root.geometry("500x500")

root.bind("<Button-1>", leftClick)
root.bind("<Button-3>", RightClick)
root.bind("<Button-2>", Scroll)

root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)



root.mainloop()
