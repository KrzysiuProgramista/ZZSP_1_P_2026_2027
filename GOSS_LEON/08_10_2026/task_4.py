number1 = float(input("write a first number"))
number2 = float(input("write a seacond number"))
number3 = input("write a operator(+, -, *, /):")
if number3 == '+':
    print('reult', number1 + number2)
elif number3 == '-':
    print('reult', number1 - number2)
elif  number3 == '*':
    print('reult', number1 * number2)
elif  number3 == '/':
    if number2 == 0:
        print("cannot divide by zero")
    else:
        print('reult', number1 / number2)
else:
    print("unknown number")
