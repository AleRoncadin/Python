from tkinter import *

root = Tk()
root.title("Calculator")

supportE = Entry(root, width=35, bg="black", fg="white", borderwidth=5)
supportE.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    if "=" in supportE.get():
        supportE.delete(0, END)
        e.delete(0, END)
        e.insert(0, number)
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)
    supportE.delete(0, END)

def buttonOperation(symbol):
    if "=" in supportE.get():
        supportE.delete(0, END)
    first_number = e.get()
    global f_num
    global math
    math = symbol
    f_num = int(first_number)
    e.delete(0, END)
    supportE.insert(END, str(first_number) + math)

def buttonEqual():
    second_number = e.get()   
    if second_number:
        e.delete(0, END)
        supportE.insert(END, str(second_number) + "=")

        if math == "+":
            e.insert(0, f_num + int(second_number))
        elif math == "-":
            e.insert(0, f_num - int(second_number))
        elif math == "*":
            e.insert(0, f_num * int(second_number))
        elif math == "/":
            e.insert(0, f_num / int(second_number))

# Define buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: buttonOperation("+"))
button_sub = Button(root, text="-", padx=41, pady=20, command=lambda: buttonOperation("-"))
button_mul = Button(root, text="x", padx=40, pady=20, command=lambda: buttonOperation("*"))
button_div = Button(root, text="/", padx=41, pady=20, command=lambda: buttonOperation("/"))

button_equal = Button(root, text="=", padx=91, pady=20, command=buttonEqual)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=buttonClear)


# Put buttons on the screen
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button0.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)

button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

button_sub.grid(row=7, column=0)
button_mul.grid(row=7, column=1)
button_div.grid(row=7, column=2)

root.mainloop()