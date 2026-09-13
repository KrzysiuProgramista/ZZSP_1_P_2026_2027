password = input("Enter a password: ")
print("Length:", len(password))
print("At least 8 characters:", len(password) >= 8)
print("Contains a number: ", any(char in "1234567890" for char in password))
