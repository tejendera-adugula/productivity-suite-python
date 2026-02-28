import tkinter as tk
from datetime import datetime
import winsound

def run_alarm():

    def check_alarm():
        alarm_time = entry.get()
        now = datetime.now().strftime("%H:%M:%S")

        if now == alarm_time:
            winsound.Beep(1000, 1000)
            label_status.config(text="⏰ Alarm Ringing!")

        root.after(1000, check_alarm)

    root = tk.Tk()
    root.title("Alarm Clock")

    tk.Label(root, text="Enter time (HH:MM:SS)").pack()

    entry = tk.Entry(root)
    entry.pack()

    label_status = tk.Label(root, text="")
    label_status.pack()

    tk.Button(root, text="Set Alarm", command=check_alarm).pack()

    root.mainloop()


if __name__ == "__main__":
    run_alarm()