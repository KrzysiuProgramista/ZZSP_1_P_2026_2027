age = int(input("Enter your age: "))

if age < 1:
    print("Incorrect Age!")
    exit()

if age < 7:
    print("Your ticket is free.")
elif age >= 7 and age < 19:
    print("Your ticket costs 15 PLN.")
elif age >= 19 and age < 65:
    print("Your ticket costs 30 PLN.")
elif age >= 65:
    print("Your ticket costs 18 PLN.")
