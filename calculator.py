import tkinter as tk

window = tk.Tk()

window.title("Calculator")

window.minsize(300,400)

math_text = tk.Label(master = window, text = "", height = 5, width = 33)
math_text.pack()

Result = False

def update_amount(number):
    if Result == False:
        current_amount = math_text.cget("text")
        if current_amount == "0":
            math_text.config(text=number)
        else:
            math_text.config(text=str(current_amount) + number)
    if Result == True:
        math_text["text"] = ""
        math_text["text"] = math_text["text"] + number

def clear_history():
    current_balance = float(math_text.cget("text"))
    withdrawal_amount = float(math_text.cget("text"))
    new_balance = current_balance - withdrawal_amount
    math_text.config(text=new_balance)
    math_text.config(text="")

history = []

def enter_amount():
    operation = math_text.cget("text")
    answer = eval(operation)
    history.append(operation)
    history.append(answer)
    math_text.config(text = answer)
    Result == True

def key_pressed(event):
    key = event.char
    if key.isdigit():
        update_amount(key)
    elif key == "+": 
        math_text["text"] = math_text["text"] + "+"
    elif key == "-":
        math_text["text"] = math_text["text"] + "-"
    elif key == "*":
        math_text["text"] = math_text["text"] + "*"
    elif key == "/":
        math_text["text"] = math_text["text"] + "÷"

def enter_button(event):
    enter = event.char
    if enter.onclick():
        update_amount(enter)
    
def clear():
    math_text.config(text = "")
    # clear = event.char
    # if clear.onclick():
    #     update_amount(clear)
    
def add():
    math_text["text"] = str(math_text["text"]) + "+"
    Result == False

def subtract():
    math_text["text"] = str(math_text["text"]) + "-"
    Result == False

def multiply():
    math_text["text"] = str(math_text["text"]) + "*"
    Result == False

def divide():
    math_text["text"] = str(math_text["text"]) + "÷"
    Result == False

button_frame = tk.Frame()
button_frame.pack()
button_frame.rowconfigure([0,1,2,3], minsize = 60)
button_frame.columnconfigure([0,1,2,3], minsize = 60)

for i in range(10):
    button = tk.Button(button_frame, text=str(i), width=5, height=2, command=lambda i=i: update_amount(str(i)))
    button.grid(row=i//3, column=i%3, sticky = "nsew")

enter = tk.Button(button_frame, text="Enter", width=5, height=2, command=enter_amount)
enter.grid(row=3, column=1, sticky = "nsew")

clear = tk.Button(button_frame, text="Clear", width=5, height=2, command=clear)
clear.grid(row=3, column=2, sticky = "nsew")

add_button = tk.Button(button_frame, text = "+", width = 5, height = 2, command = add)
add_button.grid(row = 0, column = 3, sticky = "nsew")

subtract_button = tk.Button(button_frame, text = "-", width = 5, height = 2, command = subtract)
subtract_button.grid(row = 1, column = 3, sticky = "nsew")

multiply_button = tk.Button(button_frame, text = "*", width = 5, height = 2, command = multiply)
multiply_button.grid(row = 2, column = 3, sticky = "nsew")

divide_button = tk.Button(button_frame, text = "÷", width = 5, height = 2, command = divide)
divide_button.grid(row = 3, column = 3, sticky = "nsew")

def light_mode():
    window.configure(background = "white")
    math_text["bg"] = "white"
    math_text["fg"] = "black"

def dark_mode():
    window.configure(background = "black")
    math_text["bg"] = "black"
    math_text["fg"] = "white"

window.bind("<Key>", key_pressed)

window.bind("<Return>", enter_amount)

window.mainloop()