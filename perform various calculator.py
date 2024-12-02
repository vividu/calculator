# Author: Vivi Du
# This program allows the user to perform various calculator functions. It greets the user, provides a menu to choose a function, and loops based on user choice.

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def get_user_input():
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        return number1, number2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_user_input()

def display_menu():
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    print("Welcome to the Calculator Program!")
    user_name = input("What's your name? ")
    print(f"Hello, {user_name}! Let's get started.")

    while True:
        display_menu()
        choice = input("Please choose an option (1-5): ")

        if choice == "1":
            print("\nYou chose Addition.")
            num1, num2 = get_user_input()
            result = add_numbers(num1, num2)
            print(f"The result is: {result}")
        elif choice == "2":
            print("\nYou chose Subtraction.")
            num1, num2 = get_user_input()
            result = subtract_numbers(num1, num2)
            print(f"The result is: {result}")
        elif choice == "3":
            print("\nYou chose Multiplication.")
            num1, num2 = get_user_input()
            result = multiply_numbers(num1, num2)
            print(f"The result is: {result}")
        elif choice == "4":
            print("\nYou chose Division.")
            num1, num2 = get_user_input()
            result = divide_numbers(num1, num2)
            print(f"The result is: {result}")
        elif choice == "5":
            print(f"Goodbye, {user_name}! Thanks for using the calculator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
