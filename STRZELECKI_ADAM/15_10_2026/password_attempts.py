attemps = 3
password = "Zaq@2WSX!"

while attemps > 0:
    guess = input("Enter your password: ")
    if guess == password:
        print("Login successful!")
        exit()
    else:
        print("Wrong password. Try again!")
        attemps -= 1
        print("Attempts left:", attemps)

print("You entered the wrong password 3 times! No more attempts are left.")
