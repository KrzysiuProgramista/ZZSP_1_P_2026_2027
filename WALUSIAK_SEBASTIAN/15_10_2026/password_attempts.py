correct_password = input("podaj jakie ma byc haslo")
attempts_left = 3

while attempts_left > 0:
    password = input("wpisz haslo: ")
    
    if password == correct_password:
        print("zalogowano!")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"zleee. pozostale proby: {attempts_left}")
        else:
            print("zostales zablokowany.")
