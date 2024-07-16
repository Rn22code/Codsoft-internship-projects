import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")


def mark_task_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, task + " (Completed)")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")


root = tk.Tk()
root.title("To-Do List")


frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)


listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bd=0, font="Arial 12")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)


scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)


entry_task = tk.Entry(root, font="Arial 12", width=54)
entry_task.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)


button_add_task = tk.Button(frame_buttons, text="Add Task", width=15, command=add_task)
button_add_task.grid(row=0, column=0, padx=5)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", width=15, command=delete_task)
button_delete_task.grid(row=0, column=1, padx=5)

button_mark_task = tk.Button(frame_buttons, text="Mark Completed", width=15, command=mark_task_completed)
button_mark_task.grid(row=0, column=2, padx=5)


root.mainloop()
