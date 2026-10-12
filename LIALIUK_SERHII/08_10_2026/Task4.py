num1 = int(input("Print me the first number: "))
num2 = int(input("Print me the second number: "))
op = (input("Print me either +,-,*,/: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    if num2 == 0 or num1 == 0:
        print("Cannot division by 0")
    else:
        print(num1/num2)
else:
    print("Invalid Operator")