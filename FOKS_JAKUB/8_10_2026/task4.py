num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
Operator = input("Enter an operator: ")

if Operator == "+":
    print(num1 + num2)
elif Operator == "-":
    print(num1 - num2)
elif Operator == '*':
    print(num1 * num2)
elif Operator == '/':
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")
