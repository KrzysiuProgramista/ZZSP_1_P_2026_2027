num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+,-,*,/):")

if operator == "+":
    print(num1 + num2)
elif operator =="-":
    print(num1 - num2)
elif operator =="*":
    print(num1 * num2)
elif operator =="/":
    if num2 == 0:
        print("cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("unknown operator")