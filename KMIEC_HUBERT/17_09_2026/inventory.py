magazyn_czesci = [
    ["Mlotek", 14],
    ["Srubokret", 85],
    ["Kombinerki", 32],
    ["Klucze", 19]
]

def podaj_ilosc(pozycja):
    return pozycja[1]

def podaj_nazwe(pozycja):
    return pozycja[0]

lider_magazynu = max(magazyn_czesci, key=podaj_ilosc)
print(f"Najwięcej na stanie: {lider_magazynu}")

magazyn_czesci.append(["Wiertarka", 45])

magazyn_czesci.sort(key=podaj_nazwe)
print(f"Spis alfabetyczny: {magazyn_czesci}")

# RÓŻNICE MIĘDZY METODAMI USUWANIA:
# 1. remove() -> kasuje element na podstawie jego WARTOŚCI (szuka np. słowa "Pon" i je usuwa). Nie obchodzi go indeks.
# 2. pop() -> usuwa element po jego POZYCJI (indeksie) i co ważne: "wypluwa" (zwraca) ten element, więc można go przechwycić do zmiennej.
# 3. del -> komenda systemowa, usuwa wszystko pod wskazanym indeksem na stałe, nic nie zwracając.
