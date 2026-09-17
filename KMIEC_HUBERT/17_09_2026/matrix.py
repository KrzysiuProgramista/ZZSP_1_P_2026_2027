w1 = [1, 2, 3]
w2 = [4, 5, 6]
w3 = [7, 8, 9]
siatka = [w1, w2, w3]

print(f"Rząd 1: {siatka[0]}")
print(f"Rząd 2: {siatka[1]}")
print(f"Rząd 3: {siatka[2]}")

skos = [siatka[0][0], siatka[1][1], siatka[2][2]]
print(f"Przekątna główna: {skos}")

suma_poczatek = siatka[0][0] + siatka[0][1] + siatka[0][2]
print(f"Wynik dodawania 1. wiersza: {suma_poczatek}")

