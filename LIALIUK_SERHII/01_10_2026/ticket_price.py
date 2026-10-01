Age=int(input("how old are you: "))

if Age < 7:
    print("The enter is free for you")
elif Age <18:
    print("Ticket costs 15 PLN")
elif Age < 64:
    print("Ticket costs 30 PLN")
elif Age >= 65:
    print("Ticket costs 18 PLN")
else:
    print("Invalid number or number is below zero")