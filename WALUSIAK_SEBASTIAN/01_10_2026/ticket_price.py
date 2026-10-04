age = int(input("Whats ur age?"))

if age < 7:
    print("Free")
elif age in range(7, 18):
    print("15 PLN")
elif age in range(19, 64):
    print("30 PLN")
else:
    print("18 PLN")
