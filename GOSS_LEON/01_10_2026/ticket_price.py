age = int(input('how old are you'))
if age < 7:
    print('you can come for free')
elif age >= 7 and age <= 18:
    print('your ticket costs 15PLN')
elif age >= 19 and age <= 64:
    print('your ticket costs 30PLN')
elif age >= 65:
    print('your ticket costs 18PLN')
