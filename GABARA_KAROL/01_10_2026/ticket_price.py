age = int(input("Podaj wiek: "))

if age < 7:
    print("Bilet jest darmowy")
elif age <= 18:
    print("Bilet kosztuje 15 PLN")
elif age <= 64:
    print("Bilet kosztuje 30 PLN")
else:
    print("Bilet kosztuje 18 PLN")
