h = int(input("Jak wysoka piramida: "))

for i in range(h):
    s = " " * (h - i - 1)
    g = "*" * (2 * i + 1)
    print(s + g)
