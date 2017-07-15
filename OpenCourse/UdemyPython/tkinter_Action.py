#! /usr/bin/env python3

from tkinter import *

root = Tk()

def printName():
    print("Hello there, this is Will.\n Welcome to login")


button1 = Button(root, text="Click Me", command=printName)
button1.grid(columnspan=2)

root.mainloop()
