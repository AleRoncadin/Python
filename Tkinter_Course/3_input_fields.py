from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="black", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    saluta = "Hello " + e.get()
    myLabel = Label(root, text=saluta)
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick,
                  fg = "green", bg="yellow") 
myButton.pack()

root.mainloop()