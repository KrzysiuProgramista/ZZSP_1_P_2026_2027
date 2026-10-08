num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
oper = input("Enter an operator: ")
#   :3
if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    if num2 == 0:
        print("Cannot devide by 0")
    else:
        print(num1/num2)
else:
    print("unknown operator")