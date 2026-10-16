suma = 0
ile = 0
petla = 1

while petla == 1:
    tekst = input("Podaj liczbe lub stop: ")
    
    if tekst == "stop":
        petla = 0
    else:
        liczba = float(tekst)
        suma = suma + liczba
        ile = ile + 1

if ile == 0:
    print("Nie podano zadnych liczb.")
else:
    srednia = suma / ile
    print("Ilosc liczb:", ile)
    print("Srednia:", srednia)
