Age = int(input("How old are you: "))

if Age < 8:
    print("Your ticket is free.")
elif Age > 7 and Age < 19:
    print("Your ticket costs 15 PLN.")
elif Age > 18 and Age < 65:
    print("Your ticket costs 30 PLN.")
elif Age > 64:
    print("Your ticket costs 18 PLN.")
