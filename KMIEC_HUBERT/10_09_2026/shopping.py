nazwa = input("Co kupujesz? ")
cena = float(input("Cena: "))
ile = int(input("Ilosc: "))

razem = cena * ile
print(f"{ile} x {nazwa} = {razem:.2f} PLN")


c = float(input("Podaj stopnie C: "))

f = (c * 1.8) + 32
k = c + 273.15

print("Fahrenheit:", f)
print("Kelvin:", k)


# Operator / sluzy do standardowego dzielenia i zawsze zwraca liczbe zmiennoprzecinkowa (float).
# Operator // to dzielenie calkowite, ktore odrzuca czesc ulamkowa i zaokragla wynik w dol.
print("Wynik / :", 10 / 9)
print("Wynik // :", 10 // 9)


haslo = input("Wpisz haslo: ")

dlugosc = len(haslo)
czy_dlugie = dlugosc >= 8

ma_cyfre = False
for znak in "0123456789":
    if znak in haslo:
        ma_cyfre = True

print("Dlugosc:", dlugosc)
print("Czy ma 8 znakow?:", czy_dlugie)
print("Czy ma cyfre?:", ma_cyfre)


mail = input("Podaj e-mail: ")

pozycja = mail.index("@")
login = mail[:pozycja]
domena = mail[pozycja + 1:]

print("Przed @:", login)
print("Po @:", domena)
