haslo = input("wpisz hasło ")
dlugosc = len(haslo)
dlugosc_z = dlugosc >= 8
liczba_z = any(ch in "1234567890" for ch in haslo)
print("czy znajduje się liczba/y w haśle",liczba_z)
print("wystarczająca długość",dlugosc_z)