user_password = input("Wprowadz haslo testowe: ")

rozmiar_hasla = len(user_password)
walidacja_dlugosci = rozmiar_hasla >= 8

znaleziona_cyfra = any(char.isdigit() for char in user_password)

print("Dlugosc:", rozmiar_hasla)
print("Czy ma 8 znakow?:", walidacja_dlugosci)
print("Czy ma cyfre?:", znaleziona_cyfra)
