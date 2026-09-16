email = input("Podaj swój email")

if "@" in email:
    print(email.split("@"))
else:
    print("ERROR")
