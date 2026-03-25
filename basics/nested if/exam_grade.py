marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 to 100")

else:
    if marks >= 50:
        print("Passed")

        if marks >= 80:
            print("Grade A")
        elif marks >= 60:
            print("Grade B")
        else:
            print("Grade C")

    else:
        print("Failed")