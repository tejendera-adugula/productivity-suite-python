import tkinter as tk
from tkinter import ttk
import alarm
import pomodoro
import todo_gui
import digital_clock

root = tk.Tk()
root.title("Productivity Suite")
root.geometry("500x400")
root.configure(bg="#1e1e1e")

# ---- Dark Style ----

style = ttk.Style()
style.theme_use("default")

style.configure("TNotebook", background="#1e1e1e", borderwidth=0)
style.configure(
"TNotebook.Tab",
background="#2d2d2d",
foreground="white",
padding=10
)

style.map("TNotebook.Tab", background=[("selected", "#444")])

# ---- Notebook ----

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

btn_style = {"bg": "#2d2d2d", "fg": "white", "bd": 0, "height": 2}

# ---- Alarm Tab ----

alarm_tab = tk.Frame(notebook, bg="#1e1e1e")
notebook.add(alarm_tab, text="Alarm")
tk.Button(alarm_tab, text="Open Alarm", command=alarm.run_alarm, **btn_style).pack(pady=40)

# ---- Pomodoro Tab ----

pomodoro_tab = tk.Frame(notebook, bg="#1e1e1e")
notebook.add(pomodoro_tab, text="Pomodoro")
tk.Button(pomodoro_tab, text="Open Pomodoro", command=pomodoro.run_pomodoro, **btn_style).pack(pady=40)

# ---- ToDo Tab ----

todo_tab = tk.Frame(notebook, bg="#1e1e1e")
notebook.add(todo_tab, text="To-Do")
tk.Button(todo_tab, text="Open To-Do", command=todo_gui.run_todo, **btn_style).pack(pady=40)

# ---- Clock Tab ----

clock_tab = tk.Frame(notebook, bg="#1e1e1e")
notebook.add(clock_tab, text="Clock")
tk.Button(clock_tab, text="Open Clock", command=digital_clock.run_clock, **btn_style).pack(pady=40)

root.mainloop()


