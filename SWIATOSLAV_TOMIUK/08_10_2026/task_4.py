number1 = int(input("give me first number: "))
operator = input("give me operator (*, /, +, -): ")
number2 = int(input("give me second number: "))

if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "/":
    if number2 == 0:
        print("Cannot divide by zero")
    else:
        print(number1/number2)
elif operator == "*":
    print(number1*number2)
else:
    print("unknown operator")