correct_password = "adrian67pr"
password = ""
attempts = 3

while attempts > 0 and password != correct_password:
    password = input("enter the password: ")

    if password != correct_password:
        attempts = attempts - 1
        print("attempts left:", attempts)

if password == correct_password:
    print("correct password")
else:
    print("wyjazd")