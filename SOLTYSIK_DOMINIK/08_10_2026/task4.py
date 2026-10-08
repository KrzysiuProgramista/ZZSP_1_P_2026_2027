num1 = float(input("podaj pierwszą liczbe : "))
num2 = float(input("podaj drugą liczbe : "))
operator = input("podaj opertatora")
if operator == "+":
    print (num1 + num2)
elif operator == "-":
    print (num1 - num2)
elif operator == "*":
    print (num1 * num2)
elif operator == "/":
    print (num1 / num2)
    if num2 == 0:
        print("cannot divide by 0")
    else:
        print(num1 / num2)
else:
    print("unnknown operator")