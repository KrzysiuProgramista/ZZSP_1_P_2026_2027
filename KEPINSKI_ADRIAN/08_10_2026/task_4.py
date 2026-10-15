first = float(input("first number : "))
operator = input("action (+,-,*,/) : ")
second = float(input("second numebr : "))
result = 0

if operator == "+":
    result = first + second
elif operator == "-":
    result == first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    if second == 0:
        print("NONONONOO cannot divide by zero")
    else:
        result = first / second
else:
    print("unknown operator : ", operator)

print("result : ", result)
