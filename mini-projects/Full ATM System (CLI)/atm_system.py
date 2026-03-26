balance = 1000
PIN = "1234"

while True:
    print("\n___ ATM MENU ___")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Choose an option (1-4): "))
    if choice == 1:
        print("Your balance is : ", balance)

    elif choice == 2:
        try:
            amount = int(input("Enter amount to deposit: "))
        except:
            print("Invalid input")
            continue

        if amount > 0:
            balance += amount
            print("Money deposited successfully.")
            print("Your balance is :", balance)
        else:
            print("Invalid amount")

    elif choice == 3:
        try:
            amount = int(input("Enter amount to withdraw: "))
        except:
            print("Invalid input")
            continue

        if amount <= balance:
            pin = input("Enter PIN: ")

            if pin == PIN:
                balance -= amount
                print("Withdrawal successful")
                print("Remaining balance:", balance)
            else:
                print("Incorrect PIN")
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using ATM")
        break  #For Finish the program, otherwise its again shows Menu.

    else:
        print("Invalid choice, try again")