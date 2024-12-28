import time

def countdown_timer():
    print("Would you like to start a timer? ")
    time.sleep(1.5)
    print("(y/n): ")
    cont = input().strip().lower()

    if cont == 'y':
        try:

            duration_minutes = int(input("Enter the duration in minutes: "))
            duration_seconds = int(input("Enter the duration in seconds: "))
            total_seconds = (duration_minutes * 60) + duration_seconds

            if total_seconds <= 0:
                print("Invalid. Please enter a correct value.")
                return

            print("Starting the timer!")
            time.sleep(1.5)

            while total_seconds:
                mins, secs = divmod(total_seconds, 60) 
                timer_display = f"{mins:02d}:{secs:02d}" 
                print(timer_display, end='\r')  
                time.sleep(1)
                total_seconds -= 1

            print("\nTimer complete! Time's up!")
        except ValueError:
            print("Invalid. Please enter numeric values only.")
    elif cont == 'n':
        print("No timer started. 'Til next time!")
    else:
        print("Invalid. Please restart the program.")


countdown_timer()
