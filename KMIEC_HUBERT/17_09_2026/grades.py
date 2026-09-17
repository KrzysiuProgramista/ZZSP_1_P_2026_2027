noty = [3.5, 5.0, 2.0, 4.5, 4.0, 3.0]

gora = max(noty)
dol = min(noty)

lacznie = 0
licznik = 0
for n in noty:
    lacznie += n
    licznik += 1
srednia = lacznie / licznik

print(f"Max: {gora}")
print(f"Min: {dol}")
print(f"Srednia: {round(srednia, 2)}")

noty_malejaco = list(noty)
noty_malejaco.sort()
noty_malejaco = noty_malejaco[::-1]
print(f"Pozycje: {noty_malejaco}")
