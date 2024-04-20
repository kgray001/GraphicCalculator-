import tkinter as tk

window = tk.Tk()

window.title("Calculator")

window.minsize(300,400)

math_text = tk.Label(master = window, text = "")
math_text.pack()

def update_amount(number):
    current_amount = math_text.cget("text")
    if current_amount == "0":
        math_text.config(text=number)
    else:
        math_text.config(text=current_amount + number)

def clear_history():
    current_balance = float(math_text.cget("text"))
    withdrawal_amount = float(math_text.cget("text"))
    new_balance = current_balance - withdrawal_amount
    math_text.config(text=new_balance)
    math_text.config(text="")

def enter_amount():
    current_balance = float(math_text.cget("text"))
    deposit_amount = float(math_text.cget("text"))
    new_balance = current_balance + deposit_amount
    math_text.config(text=new_balance)
    math_text.config(text="")

def key_pressed(event):
    key = event.char
    if key.isdigit():
        update_amount(key)
    elif key == "+": 
        math_text["text"] = math_text["text"] + "+"
    elif key == "-":
        math_text["text"] = math_text["text"] + "-"
    elif key == "*":
        math_text["text"] = math_text["text"] + "×"
    elif key == "/":
        math_text["text"] = math_text["text"] + "÷"

def enter_button(event):
    enter = event.char
    if enter.onclick():
        update_amount(enter)
    
def clear_button(event):
    clear = event.char
    if clear.onclick():
        update_amount(clear)
    
def add():
    math_text["text"] = math_text["text"] + "+"

def subtract():
    math_text["text"] = math_text["text"] + "-"

def multiply():
    math_text["text"] = math_text["text"] + "×"

def divide():
    math_text["text"] = math_text["text"] + "÷"

button_frame = tk.Frame()
button_frame.pack()
button_frame.rowconfigure([0,1,2,3], minsize = 60)
button_frame.columnconfigure([0,1,2,3], minsize = 60)

for i in range(10):
    button = tk.Button(button_frame, text=str(i), width=5, height=2, command=lambda i=i: update_amount(str(i)))
    button.grid(row=i//3, column=i%3, sticky = "nsew")

enter = tk.Button(button_frame, text="Enter", width=5, height=2, command=enter_amount)
enter.grid(row=3, column=1, sticky = "nsew")

clear = tk.Button(button_frame, text="Clear", width=5, height=2, command=clear_history)
clear.grid(row=3, column=2, sticky = "nsew")

add_button = tk.Button(button_frame, text = "+", width = 5, height = 2, command = add)
add_button.grid(row = 0, column = 3, sticky = "nsew")

subtract_button = tk.Button(button_frame, text = "-", width = 5, height = 2, command = subtract)
subtract_button.grid(row = 1, column = 3, sticky = "nsew")

multiply_button = tk.Button(button_frame, text = "×", width = 5, height = 2, command = multiply)
multiply_button.grid(row = 2, column = 3, sticky = "nsew")

divide_button = tk.Button(button_frame, text = "÷", width = 5, height = 2, command = divide)
divide_button.grid(row = 3, column = 3, sticky = "nsew")

def light_mode():
    return 

def dark_mode():
    return 

window.bind("<Key>", key_pressed)

window.bind("<Return>", enter_button)

window.mainloop()