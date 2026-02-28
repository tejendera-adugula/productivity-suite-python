import tkinter as tk

FILE = "tasks.txt"
tasks = []

def run_todo():

    def load_tasks():
        try:
            with open(FILE, "r") as f:
                for line in f:
                    task = line.strip()
                    tasks.append(task)
                    listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def save_tasks():
        with open(FILE, "w") as f:
            for task in tasks:
                f.write(task + "\n")

    def add_task():
        task = entry.get()
        if task:
            tasks.append(task)
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
            save_tasks()

    def delete_task():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            listbox.delete(index)
            tasks.pop(index)
            save_tasks()

    root = tk.Toplevel()
    root.title("To-Do List")
    root.geometry("300x350")

    entry = tk.Entry(root)
    entry.pack()

    tk.Button(root, text="Add Task", command=add_task).pack()
    tk.Button(root, text="Delete Task", command=delete_task).pack()

    listbox = tk.Listbox(root)
    listbox.pack(expand=True, fill="both")

    load_tasks()