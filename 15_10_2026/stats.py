tablica = []

for i in range(5):
    l = float(input("Wpisz liczbe: "))
    tablica.append(l)

suma = 0.0
najwieksza = tablica[0]
najmniejsza = tablica[0]

for numer in tablica:
    suma = suma + numer
    if numer > najwieksza:
        najwieksza = numer
    if numer < najmniejsza:
        najmniejsza = numer

srednia = suma / 5

print("Suma:", suma)
print("Srednia:", srednia)
print("Najwieksza:", najwieksza)
print("Najmniejsza:", najmniejsza)
