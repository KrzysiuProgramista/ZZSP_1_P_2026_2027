n = int(input("Podaj n: "))
licznik = 0

print(n)

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    licznik = licznik + 1

print("Liczba krokow:", licznik)
