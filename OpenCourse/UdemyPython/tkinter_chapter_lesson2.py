#! /usr/bin/env python3

from tkinter import *


root = Tk() # initialize the tkinter interface


label1 = Label(root, text="Label 1")
label2 = Label(root, text="Label 2")
label3 = Label(root, text="Label 3")
label4 = Label(root, text="Label 4")

label1.grid(row =0, column =0)
label2.grid(row =0, column =1)
label3.grid(row =1, column =0)
label4.grid(row =1, column =1)

root.mainloop()
