num1 = int(input("Print the number: "))
num2 = int(input("Print the second number: "))
op = input("Print the operator(*,/,+,-): ")

if op == "*":
    print(num1*num2)
elif op == "/":
    if num1 == 0 or num2 == 0:
        ZeroDivisionError == "Cannot divide by zero"
        print("Cannot divide by zero")
    else:
        print(num1/num2)
elif op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
else:
    print("Unknown Operator.")