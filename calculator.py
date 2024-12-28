import time
# A Calculator with a Decimal Precision in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    while True:
        print("Select an operator:")
        time.sleep(1)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter your choice: ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            time.sleep(2)
            
            if choice == '1':
                result = add(num1, num2)
                print(f"{num1:.6f} + {num2:.6f} = {result:.6f}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1:.6f} - {num2:.6f} = {result:.6f}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1:.6f} * {num2:.6f} = {result:.6f}")
            elif choice == '4':
                result = divide(num1, num2)
                
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{num1:.6f} / {num2:.6f} = {result:.6f}")
        else:
            print("Invalid input")
        
        time.sleep(1)
        
        cont = input("Do you want to perform another calculation? (y/n): ")
        if cont.lower() != 'y':
            time.sleep(1)
            print("Thanks for calculating with us!")
            break

calculator()
