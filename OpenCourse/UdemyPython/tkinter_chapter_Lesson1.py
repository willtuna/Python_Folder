#! /usr/bin/env python3

from tkinter import *


root = Tk() # initialize the tkinter interface

topFrame = Frame(root)
topFrame.pack(side = TOP)

MidFrame = Frame(root)
MidFrame.pack()

botFrame = Frame(root)
botFrame.pack(side=BOTTOM)



#theLabel = Label(root, text='This is our first Tkinter Window') # We simply initialize it
#theLabel.pack()

label1 = Label(root, text="Label 1")
label2 = Label(root, text="Label 2")
label3 = Label(root, text="Label 3")
label4 = Label(root, text="Label 4")

label1.grid(row =0, column =0)
label2.grid(row =0, column =1)
label3.grid(row =1, column =0)
label4.grid(row =1, column =1)

'''
theButton1 = Button(None,text="Bottom1", fg= 'Red')
                # layout, text in Button, color
theButton1.pack()

theButton2 = Button(None,text="Bottom2", fg= 'Blue')
                # layout, text in Button, color
theButton2.pack(fill= X) # size fit to x coordinate

theButton3 = Button(botFrame,text="Bottom3", fg= 'Black')
                # layout, text in Button, color
theButton3.pack(side=LEFT, fill = Y) # size fit o y coordinate

theButton4 = Button(botFrame,text="Bottom4", fg= 'Purple')
                # layout, text in Button, color
theButton4.pack(side=LEFT)
'''
root.mainloop()
