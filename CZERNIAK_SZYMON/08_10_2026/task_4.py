num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print('Cannot divide by zero')
    else:
        print(num1 / num2)
else:
    print('Unknown operator')
