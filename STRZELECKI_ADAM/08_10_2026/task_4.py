nr1 = float(input("Enter a number: "))
nr2 = float(input("Enter a second number"))
operator = input("Enter an operator (+, -, *, /): ")


if operator == "+":
    print(nr1 + nr2)
elif operator == "-":
    print(nr1 - nr2)
elif operator == "*":
    print(nr1 * nr2)
elif operator == "/":
    if nr2 != 0:
        print(nr1 / nr2)
    else:
        print("cannot devide by zero")
else:
    print("unknown operator")
