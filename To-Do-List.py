import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill=tk.BOTH)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
add_button.pack(fill=tk.BOTH)

listbox = tk.Listbox(root, font=("Arial", 12), selectbackground="#E2E2E2")
listbox.pack(pady=10, padx=10, fill=tk.BOTH)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_button.pack(fill=tk.BOTH)

root.mainloop()
