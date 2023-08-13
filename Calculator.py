import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "π":
        entry.insert(tk.END, math.pi)
    elif text == "√":
        entry.insert(tk.END, "sqrt(")
    elif text == "x²":
        entry.insert(tk.END, "**2")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#272727")

entry = tk.Entry(root, font=("Helvetica", 32), bd=0, bg="#3A3A3A", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=8, ipady=8)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("π", 5, 1), ("√", 5, 2), ("x²", 5, 3)
]

for label, row, col in buttons:
    button = tk.Button(
        root, text=label, padx=20, pady=20, font=("Helvetica", 16),
        bg="#434343", fg="white", bd=0, activebackground="#5E5E5E", activeforeground="white"
    )
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)

root.mainloop()
