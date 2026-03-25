marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks < 50:
    print("Failed")

elif marks >= 80:
    print("Passed - Grade A")

elif marks >= 60:
    print("Passed - Grade B")

else:
    print("Passed - Grade C")