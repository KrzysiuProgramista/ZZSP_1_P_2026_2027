age = int(input("Enter your age: "))

if age < 7:
    print("Ticket price: Free")
elif age <= 18:
    print("Ticket price: 15 PLN")
elif age <= 64:
    print("Ticket price: 30 PLN")
else:
    print("Ticket price: 18 PLN")