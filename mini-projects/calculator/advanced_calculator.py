import math

def calculator():
    while True:
        print("\n--- ADVANCED CALCULATOR ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Modulus")
        print("8. Exit")

        choice = input("Choose option (1-8): ")

        if choice == "8":
            print("Exiting calculator...")
            break

        try:
            if choice in ["1", "2", "3", "4", "5", "7"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            elif choice == "6":
                num = float(input("Enter number: "))
            else:
                print("Invalid choice")
                continue

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", num1 / num2)

        elif choice == "5":
            print("Result:", num1 ** num2)

        elif choice == "6":
            if num < 0:
                print("Cannot take square root of negative number")
            else:
                print("Result:", math.sqrt(num))

        elif choice == "7":
            print("Result:", num1 % num2)

calculator()