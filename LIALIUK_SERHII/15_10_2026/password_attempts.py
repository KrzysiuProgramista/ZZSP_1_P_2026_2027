password = "Pancakes"
attempts = 3
while attempts > 0:
    User_pass = input("Enter the password: ")
    if User_pass == password:
        print("Password granted.")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left before access will be denied.")
if attempts == 0:
    print("Too many incorrect attempts. Access denied.")
