import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# File to store tasks
TASK_FILE = "tasks.txt"

# Load tasks if file exists
tasks = []
if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]

# Functions
def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_task = simpledialog.askstring("Edit Task", "Update task:", initialvalue=tasks[index])
        if new_task:
            tasks[index] = new_task
            listbox.delete(index)
            listbox.insert(index, new_task)
            save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to edit!")

def save_tasks():
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# GUI Window
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x450")
root.resizable(False, False)

# Widgets
label = tk.Label(root, text="My To-Do List", font=("Arial", 16))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", width=15, command=edit_task)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
listbox.pack(pady=10)

# Load tasks into listbox
for task in tasks:
    listbox.insert(tk.END, task)

# Run the GUI
root.mainloop()
