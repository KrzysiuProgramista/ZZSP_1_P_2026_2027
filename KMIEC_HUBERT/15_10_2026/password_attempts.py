haslo = "sekret"
ile = 3

while ile > 0:
    odpowiedz = input("Wpisz haslo: ")
    
    if odpowiedz == haslo:
        print("Dostep przyznany!")
        ile = 0
    else:
        ile = ile - 1
        if ile > 0:
            print("Zle haslo. Zostalo prob:", ile)
        else:
            print("Konto zablokowane!")