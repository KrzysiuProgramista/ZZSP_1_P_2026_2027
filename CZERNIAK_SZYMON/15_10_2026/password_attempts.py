password = 'Joker123'
attempts = 3

while True:
    attempt = input('Enter the password:')
    if attempt != password:
        print('Wrong password')
        attempts -= 1
        print('Attempts:', attempts)
        if attempts == 0:
            print('You reached the limit')
            break
    elif attempt == password:
        print('Password is correct')
        break
