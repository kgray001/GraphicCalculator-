import tkinter as tk

window = tk.Tk()

window.title("Calculator")

math_text = tk.Label(master = window, text = "")
math_text.pack()

button_frame = tk.Frame()
button_frame.pack()

window.mainloop()