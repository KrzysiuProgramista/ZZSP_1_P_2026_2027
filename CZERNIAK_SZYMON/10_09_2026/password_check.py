password = input('Enter your password:')
print(len(password))
if len(password) < 8:
    print('Password has less than 8 characters')
else:
    print('Password has 8 or more characters')
'0' in password, '1' in password, '2' in password, '3' in password, '4' in password, '5' in password, '6' in password, '7' in password, '8' in password, '9' in password
if '0' in password or '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password:
    print('Password has a digit')
else:
    print('Password does not have a digit')
