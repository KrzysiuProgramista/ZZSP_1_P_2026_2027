dane_zakupowe = [input("Wpisz nazwe towaru: "), float(input("Podaj cene: ")), int(input("Podaj ilosc: "))]

paragon_suma = dane_zakupowe[1] * dane_zakupowe[2]
print(f"{dane_zakupowe[2]} x {dane_zakupowe[0]} = {paragon_suma:.2f} PLN")
