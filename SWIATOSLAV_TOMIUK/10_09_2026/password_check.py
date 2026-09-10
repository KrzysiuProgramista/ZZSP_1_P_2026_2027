password = input("Type password: ")
print(len(password))
print(len(password) >= 8)

has_digit = False
for char in password:
    if char in "0123456789":
        has_digit = True
print(has_digit)