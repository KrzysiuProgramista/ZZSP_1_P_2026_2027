age = int(input("Enter your age: "))

if age < 7:
    print("You get to ride for free!")
elif (age >= 7) & (age <= 18):
    print("The ticket costs 15 PLN")
elif (age >= 19) & (age <= 64):
    print("The ticket costs 30 PLN")
elif (age >= 65):
    print("The ticket costs 18 PLN")