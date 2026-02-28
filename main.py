import alarm
import stopwatch
import timer

while True:
    print("\nChoose option")
    print("1 Alarm")
    print("2 Stopwatch")
    print("3 Timer")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        alarm.run_alarm()

    elif choice == "2":
        stopwatch.run_stopwatch()

    elif choice == "3":
        timer.run_timer()

    elif choice == "4":
        print("Exiting app...")
        break

    else:
        print("Invalid choice")
