from tkinter import *

root = Tk()

label1 = Label(root, text="Enter your expression")
label1.pack()

# don't forget the event
def evaluate(event):
    data = e.get()
    # fetch the entry 
    ans.configure(text="Answer:" + str(eval(data)))
    # configure the label as the text , which start evaluate first

e = Entry(root)
e.pack()
e.bind("<Return>", evaluate)

ans = Label(root)
ans.pack()


root.mainloop()
