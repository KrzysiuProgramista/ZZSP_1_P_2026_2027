password = "masło"
attempts = 3
while attempts > 0:
    user_password = input("Enter the password: ")
    if user_password == password:
        print("Password correct!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
if attempts == 0:
    print("Too many incorrect attempts. Access denied.")
