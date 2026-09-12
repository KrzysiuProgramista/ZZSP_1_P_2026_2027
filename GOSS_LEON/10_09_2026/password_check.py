password = input("enter the password: ")
length = len(password)
at_least_8_characters = length >=8
print(f"length: {length}")
print(f"at_least_8_characters: {at_least_8_characters}")
if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
    print("password has at least one number")
