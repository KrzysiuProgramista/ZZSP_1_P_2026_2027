kalendarz = ["Pon", "Wtor", "Srod", "Czw", "Piat", "Sob", "Niedz"]

dni_robocze = kalendarz[:-2]
weekendowe = kalendarz[-2:]

print(f"Praca: {dni_robocze}")
print(f"Weekend: {weekendowe}")

odwrocone_dni = []
for dzien in kalendarz:
    odwrocone_dni.insert(0, dzien)

print(f"Wstecz: {odwrocone_dni}")

