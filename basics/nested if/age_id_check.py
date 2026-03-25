age = int(input("Enter your age: "))

if age >= 18:
    has_id = input("Do you have an ID? (yes/no): ")

    if has_id == "yes":
        print("You are allowed")
    else:
        print("ID required")
else:
    print("You must be 18+")