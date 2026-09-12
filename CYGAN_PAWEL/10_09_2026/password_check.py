password = input("Enter your password: ")
print(len(password))
if len(password) >= 8: 
 print("The password has at least 8 characters")
if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
    print("The password contains at least one digit")
