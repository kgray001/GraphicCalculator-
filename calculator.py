import tkinter as tk

window = tk.Tk()

window.title("Calculator")

window.minsize(300,400)

math_text = tk.Label(master = window, text = "")
math_text.pack()

def update_amount(number):
    current_amount = amount_label.cget("text")
    if current_amount == "0":
        amount_label.config(text=number)
    else:
        amount_label.config(text=current_amount + number)

def clear_history():
    current_balance = float(balance_label.cget("text"))
    withdrawal_amount = float(amount_label.cget("text"))
    new_balance = current_balance - withdrawal_amount
    balance_label.config(text=new_balance)
    amount_label.config(text="")

def enter_amount():
    current_balance = float(balance_label.cget("text"))
    deposit_amount = float(amount_label.cget("text"))
    new_balance = current_balance + deposit_amount
    balance_label.config(text=new_balance)
    amount_label.config(text="")

def key_pressed(event):
    key = event.char
    if key.isdigit():
        update_amount(key)

def enter_button(event):
    enter = event.char
    if enter.onclick():
        update_amount(enter)

balance_label = tk.Label(window, text="1000", font=("Arial", 16))
balance_label.pack()

amount_label = tk.Label(window, text="", font=("Arial", 14))
amount_label.pack()

button_frame = tk.Frame()
button_frame.pack()
button_frame.rowconfigure([0,1,2,3], minsize = 60)
button_frame.columnconfigure([0,1,2], minsize = 60)

for i in range(10):
    button = tk.Button(button_frame, text=str(i), width=5, height=2, command=lambda i=i: update_amount(str(i)))
    button.grid(row=i//3, column=i%3, sticky = "nsew")

enter = tk.Button(button_frame, text="Enter", width=5, height=2, command=enter_amount)
enter.grid(row=3, column=1, sticky = "nsew")

clear = tk.Button(button_frame, text="Clear", width=5, height=2, command=clear_history)
clear.grid(row=3, column=2, sticky = "nsew")

window.bind("<Key>", key_pressed)

window.bind("<Enter>", enter_button)

window.mainloop()