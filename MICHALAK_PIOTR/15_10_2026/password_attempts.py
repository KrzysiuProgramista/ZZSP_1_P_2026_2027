password = "i love musturd!!!"
i = 3
while i > 0:
    guess = input("What is the password: ")

    if guess == password:
        print("Welcome in")
        break
    else:
        i -= 1
        if i > 0:
            print("Wrong password. Attempts left", i)
        else:
            print("Account blocked")