n = int(input("Podaj dodatnia liczbe: "))
kroki = 0

while n != 1:
    print(n)

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    kroki = kroki + 1

print(1)
print("Liczba krokow:", kroki)
