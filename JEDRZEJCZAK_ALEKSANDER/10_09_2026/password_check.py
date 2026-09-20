password = input("Enter password: ")

print("Length:", len(password))
print("At least 8 characters:", len(password) >= 8)
print("Contains a digit:", any(char in "0123456789" for char in password))
