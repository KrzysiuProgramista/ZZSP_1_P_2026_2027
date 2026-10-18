liczby = []

for i in range(5):
    liczba = int(input("Podaj liczbe: "))
    liczby.append(liczba)

suma = 0

for liczba in liczby:
    suma = suma + liczba

srednia = suma / 5

najwieksza = liczby[0]
najmniejsza = liczby[0]

for liczba in liczby:
    if liczba > najwieksza:
        najwieksza = liczba

    if liczba < najmniejsza:
        najmniejsza = liczba

print("Suma:", suma)
print("Srednia:", srednia)
print("Najwieksza:", najwieksza)
print("Najmniejsza:", najmniejsza)
