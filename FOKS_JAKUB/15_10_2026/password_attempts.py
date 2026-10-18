password = "python123"
attempts = 3

while attempts > 0:
    guess = input("enter password: ")

    if guess == password:
        print("correct password")
        break
    else:
        attempts = attempts - 1

        if attempts > 0:
            print("attempts left:", attempts)
        else:
            print("account locked")
