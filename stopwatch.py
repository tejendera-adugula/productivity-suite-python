import time

def run_stopwatch():
    start_time = None

    while True:
        choice = input("1.Start 2.Stop 3.Exit: ")

        if choice == "1":
            start_time = time.time()
            print("Started")

        elif choice == "2":
            if start_time:
                elapsed = time.time() - start_time
                print("Time:", round(elapsed, 2), "seconds")

        elif choice == "3":
            break


if __name__ == "__main__":
    run_stopwatch()