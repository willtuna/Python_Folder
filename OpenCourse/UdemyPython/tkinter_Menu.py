#! /usr/bin/env python3
from tkinter import *

root = Tk()

def random():
    print("This is a statement")


# The whole bar
mainMenu = Menu(root)
root.configure(menu=mainMenu)

# this is the menu under mainmenu
subMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu = subMenu)
subMenu.add_command(label = "Random Function", command= random)
subMenu.add_command(label = "New File", command= random)

subMenu.add_separator()

subMenu.add_command(label = "Supercalafragilistic", command=random)
# Dropdown menu


root.mainloop()
