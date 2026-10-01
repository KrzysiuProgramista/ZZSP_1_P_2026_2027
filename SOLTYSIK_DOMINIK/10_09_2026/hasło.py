password = input("Enter password: ")

print("Length:", len(password))
print("At least 8 characters:", len(password) >= 8)

has_digit = False

for character in password:
    if character in "0123456789":
        has_digit = True
        break

print("Contains a digit:", has_digit)