import time
import datetime

def display_current_time():
    while True:
        print("Would you like to know the current time? ")
        time.sleep(1)
        print("(y/n): ")
        cont = input().lower()
        
        time.sleep(1)
        if cont == 'y':
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Current time: {current_time}")
                time.sleep(1)
                
        elif cont == 'n':
            print("Come back again! ")
            time.sleep(2)
            break
        
def display_real_time():
    while True:
        print("Would you like to see a real-time time display instead? ")
        time.sleep(1)
        print("(y/n): ")
        cont = input().lower()
    
        time.sleep(1)
        if cont == 'y':
            print("Displaying the real-time time (press Ctrl + C to stop): ")
            try:
                while True:
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Current time: {current_time}", end='\r')
                
            except KeyboardInterrupt:
                time.sleep(2)
                print("\nDisplaying real-time time stopped.")
            break
        
        elif cont == 'n':
            print("Thank you and come back again! ")
            time.sleep(2)
            break    

def main():
    display_current_time()
    display_real_time()
    
main()
