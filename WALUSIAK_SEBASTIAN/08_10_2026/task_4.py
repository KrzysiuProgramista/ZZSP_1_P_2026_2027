num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter an operator (+, -, *, /): ").strip()
if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 == 0:
        print("cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("unknown operator")

