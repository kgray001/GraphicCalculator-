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

def withdraw_funds():
    current_balance = float(balance_label.cget("text"))
    withdrawal_amount = float(amount_label.cget("text"))
    new_balance = current_balance - withdrawal_amount
    balance_label.config(text=new_balance)
    amount_label.config(text="")

def deposit_funds():
    current_balance = float(balance_label.cget("text"))
    deposit_amount = float(amount_label.cget("text"))
    new_balance = current_balance + deposit_amount
    balance_label.config(text=new_balance)
    amount_label.config(text="")

def key_pressed(event):
    key = event.char
    if key.isdigit():
        update_amount(key)

balance_label = tk.Label(window, text="1000", font=("Arial", 16))
balance_label.pack()

amount_label = tk.Label(window, text="", font=("Arial", 14))
amount_label.pack()

button_frame = tk.Frame()
button_frame.pack()
button_frame.rowconfigure([0,1,2,3], minsize = 50)
button_frame.columnconfigure([0,1,2], minsize = 50)

for i in range(10):
    button = tk.Button(button_frame, text=str(i), width=5, height=2, command=lambda i=i: update_amount(str(i)))
    button.grid(row=i//3, column=i%3, sticky = "nsew")

withdraw_button = tk.Button(button_frame, text="Withdraw", width=10, height=2, command=withdraw_funds)
withdraw_button.grid(row=4, column=0)

deposit_button = tk.Button(button_frame, text="Deposit", width=10, height=2, command=deposit_funds)
deposit_button.grid(row=4, column=1)

window.bind("<Key>", key_pressed)


window.mainloop()