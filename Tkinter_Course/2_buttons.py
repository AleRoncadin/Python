from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Ciao")
    myLabel.pack()

myButton = Button(root, text="CLICCAMI!", padx=50, pady=50, command=myClick,
                  fg = "green", bg="yellow") 
# ,state = DISABLED per disattivarlo
# non devi mettere le parentesi nelle funzioni dopo command=

myButton.pack()

root.mainloop()