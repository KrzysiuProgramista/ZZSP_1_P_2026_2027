c_pass = "prog2137"
att = 3

while att > 0:
    passw = input("enter the password: ")

    if passw == c_pass:
        print("access granted")
        break
    else:
        att -= 1

        if att > 0:
            print("incorrect password")
            print("attempts left:", att)
        else:
            print("incorrect pass")
            print("account locked")