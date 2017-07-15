from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_arc(10,10,200,80, extent=359, style=ARC )
#               x1,y1, x2,y2(rectangle),degree of arc 
canvas.create_arc(10,10,150,150, extent=180, style=ARC )
#               x1,y1, x2,y2(rectangle) 


#text cerateion
canvas.create_text(150,150, text ="This is my first text in tkinter", font=("DejaVu Sans Mono", 20), fill="Blue")


root.mainloop()

