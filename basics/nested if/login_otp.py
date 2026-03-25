username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    otp = input("Enter OTP: ")

    if otp == "0000":
        print("Login successful")
    else:
        print("Invalid OTP")
else:
    print("Invalid login")