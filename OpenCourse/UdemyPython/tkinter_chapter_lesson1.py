#! /usr/bin/env python3
from tkinter import *

root = Tk()

label1 = Label(root, text= "Name:")

label1.grid(row=0, column=0)

label2 = Label(root, text= "Password:")

label2.grid(row=1, column=0)


entrySpace1 = Entry(root)
entrySpace1.grid(row=0, column=1)
entrySpace2 = Entry(root)
entrySpace2.grid(row=1, column=1)


cbuttom = Checkbutton(root, text= "Remember name")
cbuttom.grid(columnspan = 2)


root.mainloop()
