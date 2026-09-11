password = input("Enter password: ")

password_length = len(password)
is_long_enough = password_length >= 8

print(f"Length: {password_length}")
print(f"At least 8 characters: {is_long_enough}")
