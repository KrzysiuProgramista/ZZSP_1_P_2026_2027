haslo = "python"
proby = 0

while proby < 3:
    wpisane = input("Podaj haslo: ")

    if wpisane == haslo:
        print("Dobre haslo!")
        break
    else:
        proby = proby + 1
        print("Zle haslo.")
        print("Pozostalo prob:", 3 - proby)

if proby == 3:
    print("Konto zablokowane!")
