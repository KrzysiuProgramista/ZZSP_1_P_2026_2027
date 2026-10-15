password = "szyszektogoat"
attempts = 0

while attempts < 3:
    key = input("put password here: ")

    if key == password:
        print("correct password")
        break
    else:
        attempts += 1
        print("wrong password  attempts left:", 3 - attempts)

if attempts == 3:
   print("blocked account")
