from tkinter import *

root = Tk()

#creo la label
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Ale")

# lo mostro a schermo
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()