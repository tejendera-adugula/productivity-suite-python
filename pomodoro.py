import tkinter as tk

def run_pomodoro():

    WORK = 25 * 60
    time_left = WORK
    running = False

    def update_timer():
        nonlocal time_left, running
        if running and time_left > 0:
            mins, secs = divmod(time_left, 60)
            label.config(text=f"{mins:02}:{secs:02}")
            time_left -= 1
            root.after(1000, update_timer)

    def start():
        nonlocal running
        running = True
        update_timer()

    def reset():
        nonlocal time_left, running
        running = False
        time_left = WORK
        label.config(text="25:00")

    root = tk.Toplevel()
    root.title("Pomodoro Timer")
    root.geometry("300x200")

    label = tk.Label(root, text="25:00", font=("Arial", 40))
    label.pack()

    tk.Button(root, text="Start", command=start).pack()
    tk.Button(root, text="Reset", command=reset).pack()