import tkinter as tk
import random
import string

def generate_password():
    length = int(length_var.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    chars = ""
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    if not chars:
        result_label.config(text="Please select at least one option.")
        return

    generated_password = ''.join(random.choice(chars) for _ in range(length))
    result_label.config(text=generated_password)

root = tk.Tk()
root.title("Password Generator")

window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

length_var = tk.StringVar(value="12")
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=False)

length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root, textvariable=length_var)
lowercase_check = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
uppercase_check = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var)
special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
result_label = tk.Label(root, text="", wraplength=300, justify="center", font=("Arial", 12))

length_label.pack(pady=5)
length_entry.pack(pady=5)
lowercase_check.pack()
uppercase_check.pack()
digits_check.pack()
special_chars_check.pack()
generate_button.pack(pady=10)
result_label.pack(pady=10)

root.mainloop()
