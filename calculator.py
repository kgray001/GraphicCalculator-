import tkinter as tk

window = tk.Tk()

window.title("Calculator")

window.minsize(260,385)

math_text = tk.Label(master = window, text = "", height = 5, width = 33)
math_text.pack()

Result = False

def update_amount(number):
    global Result
    if Result == True:
        math_text["text"] = ""
        math_text["text"] = math_text["text"] + number
        Result = False
    elif Result == False:
        math_text["text"] = math_text["text"] + number

def clear_history(event):
    current_balance = float(math_text.cget("text"))
    withdrawal_amount = float(math_text.cget("text"))
    new_balance = current_balance - withdrawal_amount
    math_text.config(text=new_balance)
    math_text.config(text="")

history_list = []

class History:
    def __init__(self, operation, result):
        self.operation = operation
        self.result = result
    
    def print_history(self):
        tuple = (self.operation, self.result)
        return f"{tuple[0]}\n {tuple[1]}\n\n"

def enter_amount():
    global Result
    operation = math_text.cget("text")
    answer = eval(operation)
    h1 = History(operation, answer)
    history_list.append(h1)
    math_text.config(text = answer)
    Result = True

def enter_key(event):
    global Result
    operation = math_text.cget("text")
    answer = eval(operation)
    h1 = History(operation, answer)
    history_list.append(h1)
    math_text.config(text = answer)
    Result = True

def key_pressed(event):
    global Result
    key = event.char
    if key.isdigit():
        if Result == True:
            math_text["text"] = ""
        update_amount(key)
        Result = False
    elif key == "+": 
        math_text["text"] = str(math_text["text"]) + "+"
        Result = False
    elif key == "-":
        math_text["text"] = str(math_text["text"]) + "-"
        Result = False
    elif key == "*":
        math_text["text"] = str(math_text["text"]) + "*"
        Result = False
    elif key == "/":
        math_text["text"] = str(math_text["text"]) + "/"
        Result = False
    elif key == "(":
        math_text["text"] = str(math_text["text"]) + "("
        Result = False
    elif key == ")":
        math_text["text"] = str(math_text["text"]) + ")"
        Result = False

def enter_button(event):
    enter = event.char
    if enter.onclick():
        update_amount(enter)

def clear(event):
    math_text.config(text = "")
    clear = event.char
    if clear.onclick():
        update_amount(clear)

def clear_btn():
    math_text.config(text = "")
    
def add():
    math_text["text"] = str(math_text["text"]) + "+"
    global Result
    Result = False

def subtract():
    global Result
    math_text["text"] = str(math_text["text"]) + "-"
    Result = False

def multiply():
    global Result
    math_text["text"] = str(math_text["text"]) + "*"
    Result = False

def divide():
    global Result
    math_text["text"] = str(math_text["text"]) + "/"
    Result = False

button_frame = tk.Frame()
button_frame.pack()
button_frame.rowconfigure([0,1,2,3], minsize = 60)
button_frame.columnconfigure([0,1,2,3], minsize = 60)

buttons = []

for i in range(10):
    button = tk.Button(button_frame, text=str(i), width=5, height=2, command=lambda i=i: update_amount(str(i)))
    button.grid(row=i//3, column=i%3, sticky = "nsew")
    buttons.append(button)

enter = tk.Button(button_frame, text="=", width=5, height=2, command=enter_amount)
enter.grid(row=3, column=1, sticky = "nsew")

clear_button = tk.Button(button_frame, text="Clear", width=5, height=2, command=clear_btn)
clear_button.grid(row=3, column=2, sticky = "nsew")

add_button = tk.Button(button_frame, text = "+", width = 5, height = 2, command = add)
add_button.grid(row = 0, column = 3, sticky = "nsew")

subtract_button = tk.Button(button_frame, text = "-", width = 5, height = 2, command = subtract)
subtract_button.grid(row = 1, column = 3, sticky = "nsew")

multiply_button = tk.Button(button_frame, text = "*", width = 5, height = 2, command = multiply)
multiply_button.grid(row = 2, column = 3, sticky = "nsew")

divide_button = tk.Button(button_frame, text = "÷", width = 5, height = 2, command = divide)
divide_button.grid(row = 3, column = 3, sticky = "nsew")

window.bind("<Key>", key_pressed)

window.bind("<Return>", enter_key)

window.bind("<BackSpace>", clear)

window.bind("<(>", key_pressed)

window.bind("<)>", key_pressed)

def light_mode():
    window.configure(background = "white")
    math_text["bg"] = "white"
    math_text["fg"] = "black"
    for button in buttons:
        button["bg"] = "white"
        button["fg"] = "black"
    enter["bg"] = "white"
    enter["fg"] = "black"
    clear_button["bg"] = "white"
    clear_button["fg"] = "black"
    add_button["bg"] = "white"
    add_button["fg"] = "black"
    subtract_button["bg"] = "white"
    subtract_button["fg"] = "black"
    multiply_button["bg"] = "white"
    multiply_button["fg"] = "black"
    divide_button["bg"] = "white"
    divide_button["fg"] = "black"
    theme_button["bg"] = "white"
    theme_button["fg"] = "black"
    history_button["bg"] = "white"
    history_button["fg"] = "black"

def dark_mode():
    window.configure(background = "black")
    math_text["bg"] = "black"
    math_text["fg"] = "white"
    for button in buttons:
        button["bg"] = "black"
        button["fg"] = "white"
    enter["bg"] = "black"
    enter["fg"] = "white"
    clear_button["bg"] = "black"
    clear_button["fg"] = "white"
    add_button["bg"] = "black"
    add_button["fg"] = "white"
    subtract_button["bg"] = "black"
    subtract_button["fg"] = "white"
    multiply_button["bg"] = "black"
    multiply_button["fg"] = "white"
    divide_button["bg"] = "black"
    divide_button["fg"] = "white"
    theme_button["bg"] = "black"
    theme_button["fg"] = "white"
    history_button["bg"] = "black"
    history_button["fg"] = "white"

def change_theme():
    theme_window = tk.Tk()
    theme_window.title("Change Theme")
    theme_window.minsize(100, 50)
    theme_window.rowconfigure([0], minsize = 75)
    theme_window.columnconfigure([0,1], minsize = 75)
    lightmode_button = tk.Button(master = theme_window, text = "Light Mode", width = 5, height = 2, command = light_mode)
    lightmode_button.grid(row = 0, column = 0, sticky = "nsew")
    darkmode_button = tk.Button(master = theme_window, text = "Dark Mode", width = 5, height = 2, command = dark_mode)
    darkmode_button.grid(row = 0, column = 1, sticky = "nsew")

theme_button = tk.Button(button_frame, text = "Color Theme", width = 5, height = 2, command = change_theme)
theme_button.grid(row = 4, columnspan = 2, column = 2, sticky = "nsew")

def record_history():
    history_window = tk.Tk() 
    history_window.title("History")
    history_window.minsize(400, 150)
    history_window.maxsize(400,150)
    # https://www.youtube.com/watch?v=0WafQCaok6g
    outer_frame = tk.Frame(master = history_window)
    outer_frame.pack(fill = tk.BOTH, expand = 1)
    history_canvas = tk.Canvas(master = outer_frame)
    history_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
    s = tk.Scrollbar(master = outer_frame, orient = tk.VERTICAL, command = history_canvas.yview)
    s.pack(side = tk.RIGHT, fill = tk.Y)
    history_canvas.configure(yscrollcommand = s.set)
    history_canvas.bind("<Configure>", lambda e: history_canvas.configure(scrollregion=history_canvas.bbox("all")))
    scrollframe = tk.Frame(master = history_canvas)
    history_canvas.create_window((0,0), window = scrollframe, anchor = "nw")
    for x in history_list:
        a = str(x.print_history())
        tk.Label(master = scrollframe, text = a).pack()

history_button = tk.Button(button_frame, text = "History", width = 5, height = 2, command = record_history)
history_button.grid(row = 4, columnspan = 2, sticky = "nsew")

class Application ():     

    def __init__ (self):
       window.bind("<Delete>", self.quit)

    def quit (self,n):
       window.destroy()

calculator = Application()

window.mainloop()