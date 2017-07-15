#! /usr/bin/env python3

from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Message !!!", "Did you know the World just blew up ?")

answer = tkinter.messagebox.askquestion("Question1", "Are you human ?")

# answer from askquestion only take "yes" or "no"
if answer == "yes":
    tkinter.messagebox.showinfo("Message !!!", "Thank god ! It's good to see you") 
if answer == "no":
    tkinter.messagebox.showinfo("Alien" , "You are a 100% confirmed Alien")


root.mainloop()
