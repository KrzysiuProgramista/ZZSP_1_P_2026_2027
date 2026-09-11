odczyt_c = float(input("Wpisz temperature w C: "))

konwersja = {
    "F": (odczyt_c * 180 / 100) + 32,
    "K": odczyt_c + 273.15
}

print("Fahrenheit:", konwersja["F"])
print("Kelvin:", konwersja["K"])
