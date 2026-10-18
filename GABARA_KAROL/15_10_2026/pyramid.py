wysokosc = int(input("Podaj wysokosc piramidy: "))

for i in range(1, wysokosc + 1):
    print(" " * (wysokosc - i) + "*" * (2 * i - 1))
