Password = input("Type your new password: ")

print("Length =",len(Password))

Password_Len = len(Password)

if Password_Len >= 8:
    print("Password is atleast 8 characters long!")

if Password in "0123456789":
    print("its contains the digits")