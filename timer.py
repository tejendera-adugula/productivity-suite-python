import time

def run_timer():
    seconds = int(input("Enter seconds: "))

    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

    print("⏰ Time up!")


if __name__ == "__main__":
    run_timer()