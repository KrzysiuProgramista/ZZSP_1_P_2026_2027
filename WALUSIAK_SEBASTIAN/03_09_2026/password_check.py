password = input("Podaj hasło")
length = len(password)
length = int(length)

if length < 8:
    print("Hasło musi mieć 8 znaków")
elif "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
    print("Hasło prawidłowe")
else:
    print("Hasło musi mieć 8 znaków i przynajmmniej 1 cyfre")
