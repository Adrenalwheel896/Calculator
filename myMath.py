import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Function to find modulus of two numbers
def mod(x, y):
    return x % y

# Function to find square root of a number
def sqrt(x):
    return math.sqrt(x)

# function to get input from the user
def get_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num <= 100:
                return num
            else:
                print("Enter a number between 1 and 100")
        except ValueError:
            print("Invalid input. Enter a valid integer.")

# Main program
                  
if __name__ == '__main__':
    print("#### Welcome to My Calculator ####")
    print("a. add(x, y)")
    print("b. subtract(x, y)")
    print("c. multiply(x, y)")
    print("d. divide(x, y)")
    print("e. mod(x, y)")
    print("f. sqrt(x)")
    print("x. exit")

while True:
    choice = input("Choice: ")
    if choice == 'x':
        print("Thanks for using MyCalculator!")
        break
    elif choice in ('a', 'b', 'c', 'd', 'e', 'f'):
        x = int(input("x: "))
        if x < 0:
            print("Warning: x must be greater than or equal to 0.")
            continue
        if choice in ('a', 'b', 'c', 'd', 'e'):
            y = int(input("y: "))
            if y < 0:
                print("Warning: y must be greater than or equal to 0.")
                continue
        if choice == 'a':
            result = add(x, y)
        elif choice == 'b':
            result = subtract(x, y)
        elif choice == 'c':
            result = multiply(x, y)
        elif choice == 'd':
            result = divide(x, y)
        elif choice == 'e':
            result = mod(x, y)
        else:
            result = sqrt(x)
        print(f"{x} {choice} {y} = {result}")
    else:
        print("Invalid choice, please try again.")