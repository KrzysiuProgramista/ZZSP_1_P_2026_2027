dni = [
    "poniedziałek",
    "Wtorek",
    "Środa",
    "czwartek",
    "Piątek",
    "Sobota",
    "niedziela"
]
dni_robocze = dni[:5]
print("Dni robocze:", dni_robocze)
weekend = dni[5:]
print("Weekend:", weekend)
print("Odwrotnie:", dni[::-1])
#remove() usuwa element na podstawie jego wartości.
#pop() usuwa element na podstawie jego indeksu i zwraca usunięty element.