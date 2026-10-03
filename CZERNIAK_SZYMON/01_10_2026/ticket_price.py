age = int(input('What is your age?:'))

if age < 7:
    print('Free ticket for you.')
elif 7 <= age <= 18:
    print('That will be 15 PLN.')
elif 19 <= age <= 64:
    print('That will be 30 PLN.')
elif age >= 65:
    print('That will be 18 PLN.')
