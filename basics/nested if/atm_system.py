balance = 1000
amount = int(input("Enter amount to withdraw: "))

if amount <= balance:
    pin = input("Enter PIN: ")

    if pin == "1234":
        print("Withdrawal successful")
    else:
        print("Incorrect PIN")
else:
    print("Insufficient balance")