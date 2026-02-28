import tkinter as tk
from datetime import datetime

def run_clock():

    def update_time():
        now = datetime.now().strftime("%H:%M:%S")
        label.config(text=now)
        root.after(1000, update_time)

    root = tk.Toplevel()
    root.title("Digital Clock")
    root.geometry("300x150")

    label = tk.Label(root, font=("Arial", 40))
    label.pack(expand=True)

    update_time()