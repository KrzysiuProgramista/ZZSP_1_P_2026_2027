password = input("Input password please: ")

print(len(password))
print("Is 8 characters long: ",end="")
#checks if password is long enough
if len(password) >= 8:
    print(True)
else:
    print(False)

#checks if password contains a digit
contains_digit = any(char.isdigit() for char in password)
print("Contains digits:", contains_digit)

